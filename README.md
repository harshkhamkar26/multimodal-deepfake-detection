# Multimodal Deepfake Detection

> **Research Project:** Robust Multimodal Audio-Visual Deepfake Detection with Cross-Manipulation Generalization

## 1. Overview

This project investigates whether combining visual and acoustic evidence can improve the robustness of deepfake detection compared with unimodal detectors. The system is designed as a reproducible research and engineering project rather than a single benchmark classifier.

The planned system will analyze a video through two complementary pipelines:

- **Visual pipeline:** sampled frames → face/region preprocessing → visual representation → visual authenticity evidence.
- **Audio pipeline:** extracted speech/audio → signal preprocessing → acoustic representation → audio authenticity evidence.
- **Fusion layer:** combines modality-specific representations/evidence to produce a final authenticity decision.
- **Explainability layer:** provides confidence and modality/region-level evidence where technically supported.

A central research question is whether multimodal fusion improves **generalization to manipulation conditions that differ from those seen during training**, rather than merely improving performance on an in-distribution test split.

## 2. Research Questions

1. How much does audio contribute to deepfake detection beyond visual evidence alone?
2. Does multimodal fusion outperform strong video-only and audio-only baselines?
3. Which fusion strategy provides the best trade-off between performance, robustness, and computational cost?
4. How does performance change under cross-manipulation evaluation?
5. How does the system behave when the audio and visual modalities provide conflicting evidence?

## 3. Planned Experimental Structure

The project will establish controlled baselines before introducing the proposed multimodal method:

1. Video-only baseline
2. Audio-only baseline
3. Simple multimodal fusion baseline
4. Proposed multimodal fusion model
5. Ablation studies
6. Cross-manipulation/generalization evaluation
7. Robustness and failure analysis

Accuracy will **not** be treated as the sole success criterion. Evaluation will include precision, recall, F1-score, ROC-AUC, confusion matrices, calibration/confidence analysis where appropriate, and generalization results.

## 4. Dataset Policy

The primary dataset is **not frozen yet**. We are prioritizing a dataset that is freely/openly accessible for academic use, contains paired audio and visual information, provides real and manipulated examples with usable labels, and is practical to download and process on available hardware.

Previously considered datasets such as FakeAVCeleb remain useful references, but FakeAVCeleb requires a request/approval process and therefore is not treated as the primary dataset unless access is actually obtained.

Current dataset candidates and the selection criteria are documented in [`docs/research/DATASET_SELECTION.md`](docs/research/DATASET_SELECTION.md).

## 5. System Engineering Goals

- Modular audio and visual processing pipelines
- Reproducible preprocessing and training configuration
- Identity-aware and leakage-resistant dataset splitting
- Version-controlled experiments and results
- Clear separation between research code and application/deployment code
- Explainable, auditable inference output where supported
- Documentation suitable for academic review and technical demonstration

## 6. Repository Structure

```text
multimodal-deepfake-detection/
├── docs/                  # Requirements, SRS, UML, architecture, research documentation
├── src/                   # Production-oriented Python package
├── tests/                 # Automated tests
├── experiments/           # Experiment configurations and experiment records
├── notebooks/             # Exploratory analysis only
├── configs/               # Reproducible configuration files
├── scripts/               # CLI utilities and pipeline scripts
├── results/               # Lightweight result summaries and figures
├── data/                  # Dataset documentation; raw datasets are not committed
├── .gitignore
├── README.md
└── LICENSE
```

## 7. Requirements and Research Documents

- [`docs/requirements/SRS.md`](docs/requirements/SRS.md) — current Software Requirements Specification
- [`docs/requirements/PROJECT_SCOPE.md`](docs/requirements/PROJECT_SCOPE.md) — project scope and functional/non-functional requirements
- [`docs/research/DATASET_SELECTION.md`](docs/research/DATASET_SELECTION.md) — dataset candidates, access constraints and selection policy
- [`docs/research/RESEARCH_PLAN.md`](docs/research/RESEARCH_PLAN.md) — research plan
- [`docs/research/RISK_AND_VALIDITY_PROTOCOL.md`](docs/research/RISK_AND_VALIDITY_PROTOCOL.md) — validity, leakage and robustness protocol

## 8. Development Method

Development will proceed in milestones:

- **M0:** project definition, requirements, UML and system architecture
- **M1:** dataset strategy and preprocessing pipeline
- **M2:** visual baseline
- **M3:** audio baseline
- **M4:** multimodal baseline
- **M5:** proposed fusion architecture
- **M6:** optimization and controlled experiments
- **M7:** ablation, cross-manipulation and robustness studies
- **M8:** explainability and error analysis
- **M9:** inference application/demo
- **M10:** reproducibility package and research paper

## 9. Research Integrity

The project will prioritize valid experimental methodology over inflated benchmark numbers. In particular, we will explicitly consider identity leakage, duplicate/source-video leakage, class imbalance, manipulation-specific artifacts, distribution shift, and limitations of dataset-based evaluation.

## 10. Status

**Current milestone: M0 — Project Definition & System Architecture / Dataset Verification.**

The problem definition, multimodal research direction and SRS are established. The primary dataset will be frozen only after a free/open candidate has been practically verified. Raw datasets will not be committed to this repository.
