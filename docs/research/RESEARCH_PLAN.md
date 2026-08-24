# M0 — Research Plan

## Core Research Question

**Does audio-visual multimodal fusion improve the robustness of deepfake detection under manipulation and distribution conditions that differ from those represented in training?**

## Supporting Questions

1. What is the marginal contribution of audio over a strong visual baseline?
2. What is the marginal contribution of visual evidence over a strong audio baseline?
3. Does learned fusion outperform simple score/feature fusion?
4. Does the proposed fusion remain useful under unseen manipulation conditions?
5. When modalities disagree, can the system identify or quantify the uncertainty reliably?

## Experimental Ladder

### E0 — Data and Split Validation

Validate source/identity relationships, class balance, duplicate risk, and train/validation/test separation before model training.

### E1 — Video Baseline

Train and evaluate a visual detector. Record all metrics and compute resource requirements.

### E2 — Audio Baseline

Train and evaluate an audio detector using a representation justified by the dataset and available compute.

### E3 — Simple Fusion Baseline

Combine modality outputs or embeddings with a simple, transparent fusion mechanism.

### E4 — Proposed Fusion

Introduce the research fusion method only after E1–E3 are stable. The proposed method must be motivated by a specific limitation of the baselines.

### E5 — Ablation

Remove or simplify components of the proposed model to establish which design choices actually matter.

### E6 — Cross-Manipulation / Distribution Shift

Train under defined manipulation conditions and evaluate under a different manipulation condition or distribution, provided the dataset supports a clean protocol.

### E7 — Modality Disagreement

Construct or identify cases in which audio and video provide different authenticity signals and measure model behavior.

### E8 — Robustness

Evaluate selected perturbations such as compression, reduced resolution, audio quality changes, or temporal sampling changes where feasible.

### E9 — Error Analysis

Inspect false positives, false negatives, calibration, identity effects, and possible shortcut learning.

## Evaluation Metrics

Primary:

- ROC-AUC
- F1-score
- Precision
- Recall
- Accuracy

Additional where appropriate:

- PR-AUC
- Equal Error Rate (for suitable binary scoring settings)
- Calibration metrics
- Per-condition metrics
- Confusion matrices
- Inference latency and resource usage

## Required Comparisons

| System | Purpose |
|---|---|
| Video-only | Visual baseline |
| Audio-only | Acoustic baseline |
| Simple fusion | Establish whether naive multimodality helps |
| Proposed fusion | Test research contribution |
| Proposed fusion - ablated | Establish component contribution |
| Cross-condition evaluation | Test robustness/generalization |

## Validity Controls

- Split by source identity where applicable.
- Check for duplicate or near-duplicate samples.
- Avoid preprocessing that leaks test information into training.
- Keep test data isolated until evaluation.
- Report class distribution.
- Use the same evaluation protocol for competing methods.
- Report uncertainty or confidence intervals when feasible.
- Record failed experiments rather than selectively reporting only favorable results.

## Publication Positioning

The paper should not claim that the proposed model is universally state of the art unless a fair, current, directly comparable benchmark establishes that claim. The intended contribution is a rigorous multimodal architecture and evaluation study emphasizing generalization, ablation, and modality behavior.

## Current Decision Gates

**Gate 1:** Scope and requirements approved.

**Gate 2:** Dataset and split protocol approved.

**Gate 3:** Baselines reproducible.

**Gate 4:** Proposed fusion justified by baseline evidence.

**Gate 5:** Generalization and ablation results complete.

**Gate 6:** Deployment/demo only after research evaluation is frozen.
