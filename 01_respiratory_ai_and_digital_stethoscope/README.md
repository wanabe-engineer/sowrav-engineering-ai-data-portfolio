# Respiratory AI and Digital Stethoscope Research

This is the flagship research section of the portfolio.

## Technical Theme

Low-cost pediatric respiratory monitoring using self-assembled digital stethoscope hardware, Raspberry Pi acquisition, signal processing, and machine learning.

## Evidence Included

- Respiratory Inductance Plethysmography literature/review materials.
- Digital stethoscope and pediatric pneumonia research drafts.
- ICT Innovation Fund proposal/progress/IRB materials.
- Conference and poster materials.
- Capstone-adjacent reports related to respiratory sensing and biomedical signal analysis.

## Master's-Level README Narrative

### Research Objective

Develop an accessible respiratory sound collection and analysis workflow for low-resource clinical settings, with emphasis on pediatric pneumonia support, signal quality, and machine learning reproducibility.

### Methodology

The central pipeline can be presented as:

1. Hardware acquisition using a low-cost self-assembled digital stethoscope.
2. Signal collection from pediatric respiratory cases under supervised clinical/research conditions.
3. Preprocessing and quality assessment of respiratory recordings.
4. Feature extraction from waveform/time-frequency representations.
5. Model training using 1D-CNN or related deep learning architectures.
6. Evaluation through accuracy, sensitivity, specificity, confusion matrix, and clinically conservative error analysis.

Useful mathematical framing:

```text
x[n] -> preprocessing -> feature tensor X -> f_theta(X) -> y_hat
```

For classification:

```latex
\hat{y} = \arg\max_k p_\theta(y=k \mid X)
```

For model evaluation:

```latex
\text{Sensitivity} = \frac{TP}{TP + FN}, \quad
\text{Specificity} = \frac{TN}{TN + FP}
```

### AI/Data Science Value

This project is strong for Data Science and Engineering graduate applications because it combines:

- Real signal acquisition.
- Biomedical hardware constraints.
- Clinical workflow awareness.
- Machine learning.
- Dataset quality issues.
- Responsible AI framing.

## Best GitHub Upgrade

Add a synthetic or public-data demo notebook that reproduces the signal-processing workflow without exposing private pediatric recordings. Use public lung-sound data or toy audio and clearly state that private clinical data are not included.

