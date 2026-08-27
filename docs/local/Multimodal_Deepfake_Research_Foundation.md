# Multimodal Deepfake Detection System

## Research Foundation, Proposed Contributions & GitHub Structure

**Date:** 27 August 2026

> Note: This Markdown version is the repository-friendly record of the research foundation. The Word document is kept locally for personal/project documentation.

## 1. Project Research Direction

The project is positioned as an explainable, robustness-aware multimodal audio-visual deepfake detection system. The objective is not simply to classify videos as real or fake, but to investigate whether combining visual evidence, audio evidence, and cross-modal consistency can improve generalization, robustness, and interpretability.

## 2. Existing Research We Are Building On

- FaceForensics++ — foundational facial manipulation/deepfake benchmark.
- Celeb-DF — high-quality face-swap deepfake dataset.
- DeepFake Detection Challenge (DFDC) — large-scale deepfake detection benchmark.
- FakeAVCeleb — audio-visual deepfake dataset combining manipulated video and synthetic/real audio.
- DeepfakeBench — standardized deepfake detection benchmark and evaluation framework.
- Audio-Visual Deepfake Detection System Using Multimodal Deep Learning — combines audio and visual evidence for multimodal detection.
- AV-Deepfake1M — large-scale audio-visual deepfake dataset with multiple manipulation types.
- Multi-modal Deepfake Detection via Multi-task Audio-Visual Prompt Learning — recent multimodal approach using cross-modal information.
- Circumventing Shortcuts in Audio-visual Deepfake Detection Datasets — demonstrates the danger of models learning dataset shortcuts instead of genuine forgery evidence.
- AV-Deepfake1M++ — extends evaluation toward real-world perturbations and robustness.
- Investigating Self-Supervised Representations for Audio-Visual Deepfake Detection — recent work on stronger audio-visual representations.
- Inconsistency-aware Multimodal Deepfake Localization — focuses on multimodal inconsistency and localization.

## 3. Research Gap

We are targeting the following gaps:

1. Strong benchmark accuracy does not necessarily mean the model learned genuine deepfake evidence.
2. Multimodal systems can still struggle when audio and visual evidence conflict.
3. Models may exploit dataset-specific shortcuts or manipulation-specific artifacts.
4. Performance can degrade under compression, noise, low resolution, re-encoding, and synchronization changes.
5. Generalization to unseen manipulation techniques and unseen datasets remains important.
6. Binary real/fake predictions often provide limited human-interpretable evidence.

## 4. Proposed Contributions

### 4.1 True Multimodal Analysis
Separate visual and audio pipelines followed by multimodal fusion.

### 4.2 Cross-Modal Consistency
Explicitly analyze whether audio and visual evidence agree, including speech/lip synchronization.

### 4.3 Robustness Evaluation
Test under compression, noise, low resolution, re-encoding, and other realistic distortions.

### 4.4 Unseen-Manipulation Generalization
Evaluate on manipulation techniques not used during training.

### 4.5 Cross-Dataset Evaluation
Test whether the detector transfers beyond the dataset used for training.

### 4.6 Explainable Detection
Provide confidence and modality/region-level evidence where technically supported.

### 4.7 Ablation Studies
Measure the value of visual, audio, fusion, and cross-modal components independently.

### 4.8 Failure Analysis
Study false positives, false negatives, conflicting modalities, and dataset artifacts.

## 5. Proposed System Architecture

```text
Input Video
   |
   +----------------------+----------------------+
   |                                             |
Visual Stream                                Audio Stream
   |                                             |
Face/frame preprocessing                    Audio preprocessing
   |                                             |
Visual representation                       Acoustic representation
   |                                             |
   +----------------------+----------------------+
                          |
                 Cross-modal analysis
                          |
              Audio <-> Video consistency
                          |
                    Fusion module
                          |
                Real / Fake decision
                          |
             Confidence + explanation
```

## 6. Experimental Framework

1. Video-only baseline
2. Audio-only baseline
3. Simple multimodal fusion baseline
4. Proposed multimodal fusion model
5. Ablation studies
6. Cross-manipulation/generalization evaluation
7. Cross-dataset evaluation
8. Robustness and perturbation testing
9. Explainability evaluation
10. Failure/error analysis

Metrics should include precision, recall, F1-score, ROC-AUC, confusion matrices, calibration/confidence analysis where appropriate, and generalization/robustness results. Accuracy will not be treated as the sole success criterion.

## 7. Dataset Research Checklist

Before selecting the final dataset, investigate:

- Dataset size and class balance
- Availability and quality of audio
- Availability and quality of video
- Manipulation types and labels
- Identity information and identity-aware splitting
- Source-video and duplicate leakage risk
- Audio-video pairing quality
- Licensing and research-use constraints
- Manipulation-specific artifacts and dataset shortcuts
- Suitability for cross-manipulation and cross-dataset experiments
- Suitability for robustness/perturbation testing

## 8. Repository Research Structure

```text
docs/research/
├── README.md
├── literature-review.md
├── research-gap.md
├── proposed-novelty.md
├── research-questions.md
├── dataset-strategy.md
├── experimental-protocol.md
└── research-roadmap.md
```

## 9. GitHub Work

A separate branch named `research-foundation` was created from `main`. The research foundation was committed there, and Draft Pull Request #1 was opened against `main`.

The research foundation contains:

- Literature review and reference map
- Research gap and novelty boundaries
- Research questions and hypotheses
- Dataset selection and leakage-control strategy
- Experimental protocol
- Baselines and ablation plan
- Robustness and generalization tests
- End-to-end research roadmap
- README alignment with the research framework

**Current GitHub state:** the work is pushed to the `research-foundation` branch and is present in Draft PR #1. It has not yet been merged into `main`.

## 10. Research Integrity Rule

We will distinguish established techniques from proposed contributions. A component will not be described as novel merely because we implement it. Novelty and performance claims will be supported by controlled experiments, ablations, generalization tests, robustness analysis, and comparison with appropriate baselines.

## 11. Current Milestone

**M0 — Project Definition & System Architecture / Research Foundation**

The next major step is Dataset Research & Selection. We should compare candidate datasets systematically and freeze the dataset and evaluation protocol before implementing the model.

## 12. Immediate Next Steps

1. Finalize candidate dataset list.
2. Create a detailed dataset comparison.
3. Select primary dataset(s) and secondary cross-dataset benchmark(s).
4. Define leakage-resistant train/validation/test splitting.
5. Define manipulation-wise and cross-manipulation evaluation.
6. Define robustness perturbations.
7. Freeze the experimental protocol.
8. Begin preprocessing and baseline implementation.
