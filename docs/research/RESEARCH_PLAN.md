# M0-M10 — Research Plan

## Core Research Question

Does reliability-aware temporal audio-visual fusion improve deepfake detection robustness compared with unimodal and simple-fusion baselines under manipulation or distribution conditions that differ from training?

## Supporting Questions

1. What is the marginal contribution of audio over a visual baseline?
2. What is the marginal contribution of visual evidence over an audio baseline?
3. Does simple multimodal fusion improve over unimodal models?
4. Does reliability-aware temporal fusion add measurable value beyond simple fusion?
5. Does temporal localization identify manipulation intervals where the dataset permits?
6. When audio and video disagree, does reliability weighting behave consistently?
7. How does the system respond to missing or degraded modalities?
8. Which components remain useful under cross-manipulation or distribution shift?

## Experimental Ladder

### E0 — Dataset and Split Validation
Validate metadata, source/identity relationships, class balance, duplicates, manipulation categories and train/validation/test separation.

### E1 — Visual Baseline
Train and evaluate a visual detector.

### E2 — Audio Baseline
Train and evaluate an audio detector.

### E3 — Simple Fusion Baseline
Combine modality outputs or embeddings using a transparent fusion method.

### E4 — Proposed Reliability-Aware Temporal Fusion
Introduce temporal modeling, modality reliability estimation and dynamic audio/visual weighting.

### E5 — Ablation
Remove or simplify reliability weighting, temporal modeling, cross-modal interaction and other proposed components.

### E6 — Cross-Manipulation / Distribution Shift
Use a clean train/evaluation condition change supported by the dataset.

### E7 — Modality Disagreement
Measure behavior when audio and visual authenticity signals conflict.

### E8 — Robustness
Evaluate compression, resolution, audio degradation and temporal sampling perturbations where feasible.

### E9 — Error and Calibration Analysis
Inspect false positives, false negatives, confidence calibration, missing-modality behavior and possible shortcut learning.

### E10 — Reproducibility and Paper Package
Freeze protocols, produce tables/figures, document limitations, package configurations and prepare the research paper.

## Evaluation Metrics

Primary:
- ROC-AUC
- F1-score
- Precision
- Recall
- Accuracy

Additional where appropriate:
- PR-AUC
- EER
- calibration metrics
- confusion matrices
- per-manipulation/per-condition metrics
- inference latency
- memory/resource usage

## Required Comparisons

| System | Purpose |
|---|---|
| Video-only | Visual baseline |
| Audio-only | Audio baseline |
| Simple fusion | Multimodal baseline |
| Proposed fusion | Reliability-aware temporal method |
| Proposed without reliability | Reliability ablation |
| Proposed without temporal module | Temporal ablation |
| Proposed without cross-modal interaction | Fusion ablation |
| Cross-condition evaluation | Generalization |
| Perturbation evaluation | Robustness |

## Novel research dimensions

The implementation should investigate, rather than assume, the value of:
- temporal segment-level evidence;
- dynamic modality reliability;
- modality disagreement;
- missing/degraded modality handling;
- reproducible localization and error analysis.

## Validity Controls

- Split by identity/source where metadata supports it.
- Check duplicates and near-duplicates.
- Keep test data isolated.
- Fit training-dependent preprocessing only on training data.
- Use the same evaluation definitions for competing methods.
- Report class and manipulation distributions.
- Record failed experiments.
- Use multiple seeds where compute permits.
- Report uncertainty when materially relevant.

## Publication Positioning

The paper should describe the method and evidence actually obtained. It should not claim universal generalization or state-of-the-art status without a fair, current and directly comparable benchmark.

## Current Decision Gates

Gate 1: Scope and requirements established.

Gate 2: LAV-DF access, metadata, integrity and split protocol verified.

Gate 3: Visual, audio and simple-fusion baselines reproducible.

Gate 4: Proposed reliability-aware temporal fusion justified by baseline evidence.

Gate 5: Ablation, generalization, robustness and disagreement studies complete.

Gate 6: Final evaluation frozen.

Gate 7: Demo and paper package finalized.
