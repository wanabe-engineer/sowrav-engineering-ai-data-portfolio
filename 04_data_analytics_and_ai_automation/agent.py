import os
import sys
import time
from dataclasses import dataclass
from typing import Any

from dotenv import load_dotenv
from google import genai
from google.genai import types
from google.genai.types import Content, Part
from playwright.sync_api import Page, sync_playwright


SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 900
DEFAULT_MODEL = "gemini-2.5-computer-use-preview-10-2025"
TURN_LIMIT = 25

SAFETY_INSTRUCTION = """
You are controlling a supervised browser on behalf of the user.

You may research, compare pages, fill non-sensitive drafts, and prepare job applications.
You must stop and ask the user before any of these actions:
- Logging in to any account.
- Accepting terms, privacy policies, cookie consent, or legal agreements.
- Solving or bypassing CAPTCHA or human verification.
- Clicking Submit, Apply, Send, Post, Confirm, Pay, Purchase, or any final irreversible action.
- Sending email/messages or uploading/sharing files.
- Entering passwords, national IDs, payment details, or other highly sensitive information.

If a website blocks automation or requires human verification, say what happened and ask the user to take over.
When a task is complete, summarize what you found or prepared.
"""


@dataclass
class ActionResult:
    name: str
    ok: bool
    message: str
    extra: dict[str, str] | None = None


def denormalize_x(x: int | float) -> int:
    return int(float(x) / 1000 * SCREEN_WIDTH)


def denormalize_y(y: int | float) -> int:
    return int(float(y) / 1000 * SCREEN_HEIGHT)


def user_confirm(prompt: str) -> bool:
    answer = input(f"\nCONFIRM REQUIRED: {prompt}\nType YES to continue: ").strip()
    return answer == "YES"


def log(message: str) -> None:
    print(message, flush=True)


def maybe_pause_for_sensitive_action(name: str, args: dict[str, Any]) -> bool:
    safety_decision = args.get("safety_decision")
    if safety_decision:
        explanation = safety_decision.get("explanation", "Gemini marked this action as sensitive.")
        return user_confirm(explanation)

    text = " ".join(str(value) for value in args.values()).lower()
    sensitive_words = [
        "submit",
        "apply",
        "send",
        "post",
        "confirm",
        "pay",
        "purchase",
        "accept",
        "agree",
        "login",
        "log in",
        "sign in",
        "captcha",
        "password",
    ]
    if name in {"type_text_at", "click_at"} and any(word in text for word in sensitive_words):
        return user_confirm(f"Gemini wants to run {name} with {args}")
    return True


def execute_action(page: Page, name: str, args: dict[str, Any]) -> ActionResult:
    if not maybe_pause_for_sensitive_action(name, args):
        return ActionResult(name, False, "User denied confirmation.")

    extra = {"safety_acknowledgement": "true"} if args.get("safety_decision") else None

    try:
        if name == "open_web_browser":
            page.goto("https://www.google.com", wait_until="domcontentloaded")
        elif name == "search":
            page.goto("https://www.google.com", wait_until="domcontentloaded")
        elif name == "navigate":
            page.goto(str(args["url"]), wait_until="domcontentloaded")
        elif name == "click_at":
            page.mouse.click(denormalize_x(args["x"]), denormalize_y(args["y"]))
        elif name == "hover_at":
            page.mouse.move(denormalize_x(args["x"]), denormalize_y(args["y"]))
        elif name == "type_text_at":
            page.mouse.click(denormalize_x(args["x"]), denormalize_y(args["y"]))
            if args.get("clear_before_typing", True):
                page.keyboard.press("Control+A")
                page.keyboard.press("Backspace")
            page.keyboard.type(str(args.get("text", "")), delay=8)
            if args.get("press_enter", True):
                page.keyboard.press("Enter")
        elif name == "key_combination":
            keys = str(args["keys"]).replace("control", "Control").replace("enter", "Enter")
            page.keyboard.press(keys)
        elif name == "scroll_document":
            direction = str(args.get("direction", "down")).lower()
            if direction in {"left", "right"}:
                page.mouse.wheel(-650 if direction == "left" else 650, 0)
            else:
                page.mouse.wheel(0, -650 if direction == "up" else 650)
        elif name == "scroll_at":
            page.mouse.move(denormalize_x(args["x"]), denormalize_y(args["y"]))
            direction = str(args.get("direction", "down")).lower()
            magnitude = int(float(args.get("magnitude", 800)) / 1000 * SCREEN_HEIGHT)
            if direction in {"left", "right"}:
                page.mouse.wheel(-magnitude if direction == "left" else magnitude, 0)
            else:
                page.mouse.wheel(0, -magnitude if direction == "up" else magnitude)
        elif name == "go_back":
            page.go_back(wait_until="domcontentloaded")
        elif name == "go_forward":
            page.go_forward(wait_until="domcontentloaded")
        elif name == "wait_5_seconds":
            time.sleep(5)
        else:
            return ActionResult(name, False, f"Unsupported action: {name}")

        try:
            page.wait_for_load_state("domcontentloaded", timeout=8000)
        except Exception:
            pass
        time.sleep(1)
        return ActionResult(name, True, "Action completed.", extra=extra)
    except Exception as exc:
        return ActionResult(name, False, f"{type(exc).__name__}: {exc}")


def response_parts(candidate: Any) -> list[Any]:
    return list(candidate.content.parts or [])


def function_calls(candidate: Any) -> list[Any]:
    return [part.function_call for part in response_parts(candidate) if getattr(part, "function_call", None)]


def text_parts(candidate: Any) -> list[str]:
    return [part.text for part in response_parts(candidate) if getattr(part, "text", None)]


def make_function_response(page: Page, result: ActionResult) -> types.FunctionResponse:
    screenshot = page.screenshot(type="png")
    response_data = {
        "url": page.url,
        "status": "ok" if result.ok else "error",
        "message": result.message,
    }
    if result.extra:
        response_data.update(result.extra)

    return types.FunctionResponse(
        name=result.name,
        response=response_data,
        parts=[
            types.FunctionResponsePart(
                inline_data=types.FunctionResponseBlob(mime_type="image/png", data=screenshot)
            )
        ],
    )


def run(goal: str) -> None:
    load_dotenv()
    if not os.getenv("GEMINI_API_KEY"):
        raise SystemExit("Missing GEMINI_API_KEY. Copy .env.example to .env and paste your key.")

    client = genai.Client()
    model = os.getenv("GEMINI_MODEL", DEFAULT_MODEL)
    log(f"Using model: {model}")

    config = types.GenerateContentConfig(
        system_instruction=SAFETY_INSTRUCTION,
        tools=[
            types.Tool(
                computer_use=types.ComputerUse(
                    environment=types.Environment.ENVIRONMENT_BROWSER,
                    excluded_predefined_functions=["drag_and_drop"],
                )
            )
        ],
    )

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(viewport={"width": SCREEN_WIDTH, "height": SCREEN_HEIGHT})
        page = context.new_page()
        page.goto("https://www.google.com", wait_until="domcontentloaded")
        log("Browser opened. Sending the first screenshot to Gemini...")

        contents = [
            Content(
                role="user",
                parts=[
                    Part(text=goal),
                    Part.from_bytes(data=page.screenshot(type="png"), mime_type="image/png"),
                ],
            )
        ]

        try:
            for turn in range(1, TURN_LIMIT + 1):
                log(f"\nTurn {turn}: asking Gemini...")
                try:
                    response = client.models.generate_content(model=model, contents=contents, config=config)
                except Exception as exc:
                    log(f"Gemini API error: {type(exc).__name__}: {exc}")
                    return

                if not response.candidates:
                    log(f"Gemini returned no candidates. Full response: {response}")
                    return

                candidate = response.candidates[0]
                contents.append(candidate.content)

                for text in text_parts(candidate):
                    log(text.strip())

                calls = function_calls(candidate)
                if not calls:
                    log("\nDone.")
                    return

                function_responses = []
                for call in calls:
                    args = dict(call.args or {})
                    log(f"Action: {call.name} {args}")
                    result = execute_action(page, call.name, args)
                    log(result.message)
                    function_responses.append(make_function_response(page, result))
                    if not result.ok and result.message == "User denied confirmation.":
                        log("Stopped before a sensitive action.")
                        return

                contents.append(
                    Content(
                        role="user",
                        parts=[Part(function_response=response) for response in function_responses],
                    )
                )
        finally:
            input("\nPress Enter to close the browser...")
            browser.close()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit('Usage: python agent.py "your browser task here"')
    run(" ".join(sys.argv[1:]))
