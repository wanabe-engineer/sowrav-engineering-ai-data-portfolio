# Nice-to-Haves Before Public GitHub Release

## High Priority

- Create a public-safe CV PDF with references and phone number removed.
- Add a synthetic-data respiratory sound notebook so reviewers can run the workflow without private clinical data.
- Add one polished dashboard demo from the SLA CSVs using synthetic or anonymized data.
- Add a root `portfolio_index.md` with one-page summaries and links to each project.
- Convert DOCX-heavy sections into Markdown summaries so GitHub renders them cleanly.

## Research Portfolio Upgrades

- Add `dataset_card.md` for the lung-sound database, without exposing raw private data.
- Add `model_card.md` for the 1D-CNN pneumonia classifier.
- Add a reproducibility diagram:
  - acquisition
  - preprocessing
  - feature extraction
  - model training
  - evaluation
  - limitations
- Add public DOI links for the IEEE/MDPI publications.
- Add a `citations.bib` file.

## Data Analyst Portfolio Upgrades

- Build a clean `healthcare_sla_dashboard/` mini-project.
- Include SQL examples:
  - daily backlog
  - SLA breach risk
  - provider/documentation volume
  - turnaround time
  - team performance
- Add a dashboard screenshot.
- Add a short business case: "How I would monitor clinical documentation operations."

## Embedded Systems Upgrades

- Add block diagrams for:
  - digital stethoscope hardware
  - microcontroller aquaculture system
  - PID-controlled conveyor system
  - robotic arm project
- Add bills of materials where safe.
- Add simulation screenshots from MATLAB/Proteus/PowerWorld if available.

## Graduate Application Upgrades

- Create a private `grad_school_packet/` branch or repo with:
  - research statement
  - statement of purpose
  - professor fit sheet
  - publication list
  - one-page project summaries
- Keep professor email lists private.

## Repository Hygiene

- Keep this repository private until redaction is complete.
- Avoid uploading raw patient data, hospital forms, or unapproved IRB material.
- Use Git LFS if large PDFs or videos are kept.
- Split public projects into smaller repos once each has a clean README and reproducible demo.
