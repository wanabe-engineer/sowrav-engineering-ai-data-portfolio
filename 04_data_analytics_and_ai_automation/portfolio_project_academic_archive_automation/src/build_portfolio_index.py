from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "evidence"
OUT = ROOT / "PORTFOLIO_INDEX.md"


def read_course_rows() -> list[dict[str, str]]:
    with (EVIDENCE / "course_download_summary.csv").open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_cleanup() -> dict:
    return json.loads((EVIDENCE / "cleanup_summary.json").read_text(encoding="utf-8"))


def project_hint(folder: str) -> str:
    text = folder.lower()
    if "vlsi" in text:
        return "VLSI logic design case study"
    if "electrical services" in text:
        return "Electrical services CAD portfolio"
    if "control" in text:
        return "Control systems modeling project"
    if "power" in text or "eee 308" in text:
        return "Power systems simulation notebook"
    if "cse" in text or "programming" in text:
        return "Programming foundations portfolio"
    if "circuit" in text:
        return "Circuit analysis lab portfolio"
    if "mat" in text or "sta" in text:
        return "Data science math/statistics support evidence"
    return "Private academic evidence / supporting material"


def main() -> None:
    rows = read_course_rows()
    cleanup = load_cleanup()
    rows.sort(key=lambda r: int(r.get("FileCount", "0")), reverse=True)

    lines = [
        "# Portfolio Index From Academic Archive",
        "",
        "## Cleanup Summary",
        "",
        f"- Files after cleanup: `{cleanup.get('total_files_after_cleanup')}`",
        f"- Size after cleanup: `{cleanup.get('total_mb_after_cleanup')} MB`",
        f"- Exact duplicates removed: `{cleanup.get('removed_duplicate_files')}`",
        f"- Recovered files moved: `{cleanup.get('moved_recovered_files')}`",
        "",
        "## Course-To-Project Map",
        "",
        "| Course folder | Files | MB | Portfolio use |",
        "| --- | ---: | ---: | --- |",
    ]

    for row in rows:
        files = int(row.get("FileCount", "0"))
        if files <= 0:
            continue
        folder = row["Folder"]
        lines.append(
            f"| {folder} | {files} | {row.get('TotalMB', '0')} | {project_hint(folder)} |"
        )

    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
