# Experimental Protocol

## Principle

Every proposed improvement must be compared against a controlled baseline. Experiments will be logged with dataset version, split, seed, model configuration, preprocessing and metrics.

## Baseline ladder

### B1 — Video-only

Visual encoder + classifier.

### B2 — Audio-only

Audio/speech encoder + classifier.

### B3 — Simple multimodal baseline

Combine visual and audio representations or prediction scores using a deliberately simple fusion method.

### B4 — Proposed multimodal system

Evidence-aware fusion plus the selected cross-modal consistency mechanism.

## Ablation plan

Remove one component at a time:

- no audio
- no visual stream
- no temporal information
- no cross-modal consistency
- no robustness augmentation, if implemented
- alternative fusion mechanism

The purpose is to determine which component actually causes improvement.

## Evaluation dimensions

### Classification

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC
- confusion matrix

### Reliability

- calibration/confidence analysis where appropriate
- threshold sensitivity
- false-positive and false-negative analysis

### Generalization

- cross-manipulation testing
- cross-dataset testing where feasible
- unseen manipulation conditions

### Robustness

Measure clean versus perturbed performance for:

- compression/re-encoding
- lower resolution
- frame dropping/temporal degradation
- background audio noise
- degraded audio quality
- controlled audio/video temporal offsets

Report both the metric under perturbation and the change from the clean baseline.

## Cross-modal conflict experiments

Construct or identify cases where:

1. video evidence is suspicious but audio appears genuine;
2. audio evidence is suspicious but video appears genuine;
3. both are suspicious;
4. both are plausible but audio-video timing is inconsistent.

This isolates whether the consistency module provides information beyond independent modality scores.

## Explainability evaluation

For supported models, record:

- visual attribution/important regions
- temporal evidence or important frames
- audio evidence where technically available
- modality-level confidence
- cross-modal consistency score

Explanations will be evaluated for stability and qualitative usefulness; they will not be treated as ground-truth forensic evidence without validation.

## Statistical discipline

Where compute permits, report repeated runs or confidence intervals rather than relying on a single random seed. Compare models on matched splits and preprocessing. Keep a record of failed experiments and negative results.

## Minimum success condition

A stronger model is not considered successful merely because it has higher training or in-distribution accuracy. A convincing result should show improvement on the intended evaluation target while remaining competitive on robustness, generalization, and computational cost.
