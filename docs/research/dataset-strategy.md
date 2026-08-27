# Dataset Strategy

## Objective

Select datasets that let us answer the research questions, not simply maximize a single benchmark score.

## Candidate datasets

### FakeAVCeleb

Primary candidate for early multimodal experiments because it directly combines manipulated visual content with synthetic/cloned audio.

### AV-Deepfake1M

Candidate for large-scale multimodal training/evaluation and localization-oriented experiments where compute and licensing permit.

### FaceForensics++

Strong candidate for visual-only baselines and controlled manipulation-family experiments.

### Celeb-DF

Candidate for higher-quality visual generalization testing.

### DFDC

Candidate for broader visual-domain evaluation and cross-dataset testing.

### AV-Deepfake1M++

Candidate for robustness/perturbation evaluation if its data and protocol fit the final experimental design.

## Selection rules

Dataset choice will be finalized after checking:

- license and permitted research use
- availability and storage requirements
- audio/video pairing quality
- manipulation labels
- identity/source metadata
- train/validation/test definitions
- duplicate and near-duplicate risk
- computational feasibility
- reproducibility of preprocessing

## Leakage-control protocol

We will prefer identity-aware or source-aware splitting where metadata allows it. The same identity, source video, or derived duplicate should not appear across train and test when that would leak information.

We will document:

- exact dataset version
- selected subsets
- preprocessing code/version
- sampling rate and frame sampling policy
- train/validation/test assignment
- excluded samples and reasons
- random seeds

## Cross-dataset protocol

Where feasible, one dataset will be used for training and another for evaluation. This is a key test of distribution shift and is more informative than relying exclusively on a random in-dataset split.

## Dataset-shortcut checks

We will inspect whether labels correlate with accidental properties such as silence patterns, duration, codec, resolution, file naming, source identity or other metadata. If a shortcut is detected, it will be documented and controlled where possible.

## Raw-data policy

Raw datasets will not be committed to GitHub. The repository will contain download instructions, dataset manifests, metadata schemas and preprocessing code where redistribution permits.
