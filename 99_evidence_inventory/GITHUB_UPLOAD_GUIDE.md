# GitHub Upload Guide

This folder was built locally without API keys.

## Recommended First Upload

Create a new private GitHub repository named:

```text
sowrav-academic-data-science-portfolio
```

Then upload the contents of `github_ready_sowrav_portfolio`.

## Manual Upload Steps

1. Open GitHub in the browser.
2. Create a new private repository.
3. Do not add a README on GitHub if uploading this folder as-is.
4. Upload the folder contents, or use Git locally:

```powershell
cd "C:\Users\User\Documents\New project\github_ready_sowrav_portfolio"
git init
git add .
git commit -m "Initial curated academic and data portfolio"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/sowrav-academic-data-science-portfolio.git
git push -u origin main
```

## Before Making Public

Review every PDF/DOCX for:

- Personal phone numbers.
- Reference contact details.
- Official signatures or institutional forms.
- Patient, hospital, or IRB-sensitive material.
- Draft manuscripts that should not be public.
