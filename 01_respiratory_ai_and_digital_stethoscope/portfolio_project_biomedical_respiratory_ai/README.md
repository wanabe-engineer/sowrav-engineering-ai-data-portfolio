# Biomedical Respiratory AI and Low-Cost Digital Stethoscope

## Project Goal

Build a master's-level portfolio project around pediatric lung-sound acquisition, low-cost digital stethoscope design, and AI-assisted respiratory disease screening. This should become the flagship research project because it connects Sowrav Chowdhury's EEE background, embedded hardware, clinical AI, and Augmedix healthcare operations experience.

## Portfolio Question

Can low-cost respiratory sound acquisition hardware support reproducible AI workflows for pediatric pneumonia or abnormal lung-sound screening?

## Methodology To Build

1. Document the acquisition pipeline: sensor/microphone, Raspberry Pi or microcontroller interface, sampling assumptions, noise sources, and storage format.
2. Create a signal-processing workflow: denoising, segmentation, spectrogram/MFCC extraction, train-validation split, and quality checks.
3. Reproduce a model baseline: 1D-CNN, CNN on spectrograms, or classical ML baseline with extracted features.
4. Evaluate with clinically meaningful metrics: sensitivity, specificity, F1-score, confusion matrix, and calibration discussion.
5. Write a limitations section covering dataset size, noise, bias, consent/IRB, and deployment constraints.

## Suggested Math / Technical Framing

- Audio sample sequence: \(x[n]\), sampled at \(f_s\).
- Short-time Fourier transform:

  \[
  X(m, k) = \sum_n x[n]w[n-m]e^{-j2\pi kn/N}
  \]

- Classification objective:

  \[
  \hat{y} = \arg\max_c p_\theta(c \mid x)
  \]

## GitHub Deliverables

- `README.md` with research objective, architecture, methodology, results, and limitations.
- `notebooks/` for preprocessing and model experiments.
- `src/` for reusable feature extraction/model code.
- `docs/` for diagrams, ethics notes, and literature review summary.
- `figures/` for pipeline diagram, spectrogram examples, and confusion matrix.

## Employer Angle

Shows healthcare AI thinking, technical documentation, model evaluation, and practical awareness of deployment constraints.

## Professor Angle

Shows a research-ready bridge between biomedical signal processing, machine learning, embedded systems, and clinical validation.

## Next Build Steps

- Add a clean architecture diagram.
- Extract 2-3 representative figures from existing research documents.
- Create a synthetic/demo notebook if raw patient data cannot be published.
- Write a paper-style `docs/methodology.md`.
