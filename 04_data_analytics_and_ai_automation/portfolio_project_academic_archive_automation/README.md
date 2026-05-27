# Academic Archive Automation and Portfolio Intelligence

## Project Goal

Turn the Gmail/Classroom/Drive archive work into a data-analytics and automation project: collect messy academic evidence, clean duplicates, organize by course, build manifests, and generate portfolio recommendations.

## Source Evidence

Representative files are in `evidence/`:

- `ULAB_Classroom_Drive_Portfolio_Project_Ideas.pdf`
- `course_download_summary.csv`
- `cleanup_summary.json`

## Portfolio Question

How can unstructured academic records be converted into a clean, searchable, portfolio-ready evidence system?

## Methodology

1. Discover academic files from Classroom and Drive.
2. Organize files by course folder.
3. Hash files with SHA-256 and remove exact duplicates.
4. Create course-level summaries.
5. Generate project ideas for GitHub and graduate applications.

## Analytics Outputs

- file counts by course
- total archive size by course
- duplicate-removal count
- strongest project clusters
- portfolio priority list

## Employer Angle

This demonstrates automation, data cleaning, evidence management, and turning messy files into a structured decision system.

## Professor Angle

This shows research organization, reproducibility, and disciplined documentation.

## Build Checklist

- [ ] Run `src/build_portfolio_index.py`.
- [ ] Add charts for file count and size by course.
- [ ] Add a cleaned project-priority table.
- [ ] Publish only the summaries, not private raw coursework.
