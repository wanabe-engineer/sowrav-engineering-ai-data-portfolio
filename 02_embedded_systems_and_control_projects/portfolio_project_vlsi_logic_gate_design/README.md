# VLSI Logic Gate Design Case Study

## Project Goal

Turn EEE 426/ETE 448 VLSI Lab work into a clean portfolio case study showing transistor-level logic design, schematic/layout artifacts, lab documentation, and engineering interpretation.

## Source Evidence

Representative files are in `evidence/`:

- `AND GATE LR1.sch`
- `CMOS INVERTER.MSK`
- `SOWRAV_CHOWDHURY_183016008_OPENENDED_EEE426.pdf`

The full private archive remains in:

`ULAB_Classroom_Drive_Archive/03_drive_classroom_folder/EEE 426_ETE 448 VLSI Lab 1`

## Technical Story

This project should explain how CMOS logic gates are designed from transistor-level switching behavior to layout-level implementation. The strongest story is:

1. Define Boolean function and truth table.
2. Map the pull-up network and pull-down network.
3. Build schematic/layout evidence.
4. Discuss propagation delay, area, power, and noise margin at a conceptual level.
5. Reflect on verification limitations and next improvements.

## Methodology

- Document inverter, AND, OR, and NOR gate behavior.
- Add screenshots or exported images from the layout/schematic tools.
- Create truth tables and transistor-network diagrams.
- Add a short section on CMOS power:

  \[
  P_{dynamic} \approx \alpha C_L V_{DD}^{2} f
  \]

- Add a delay note:

  \[
  t_p \propto R_{eq} C_L
  \]

## Portfolio Deliverables

- cleaned README
- truth tables
- schematic/layout screenshots
- explanation of `.sch` and `.MSK` files
- short PDF/report summary
- optional Python table generator for truth tables

## Employer Angle

Shows attention to detail, digital design fundamentals, and ability to explain low-level technical artifacts clearly.

## Professor Angle

Shows semiconductor/digital logic background and readiness to document rigorous engineering workflows.

## Build Checklist

- [ ] Export layout/schematic images.
- [ ] Add truth-table markdown.
- [ ] Write experiment-by-experiment summary.
- [ ] Add limitations and reproducibility notes.
