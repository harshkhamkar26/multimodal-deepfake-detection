# Multimodal Deepfake Detection

> Research Project: Robust Multimodal Audio-Visual Deepfake Detection with Reliability-Aware Temporal Fusion and Cross-Manipulation Generalization

## Overview

This project studies whether combining visual and acoustic evidence can improve deepfake detection robustness compared with unimodal and simple-fusion detectors.

The current research architecture adds:
- temporal segment-level analysis;
- reliability estimation for audio and visual modalities;
- dynamic modality weighting;
- modality-disagreement analysis;
- robustness and cross-manipulation evaluation;
- restart-safe, chunked dataset preprocessing for Colab/research environments;
- explainability and error analysis.

These are research hypotheses and must be validated through controlled experiments.

## Current Dataset

**Primary dataset: LAV-DF (Localized Audio-Visual DeepFake Dataset).**

Status: selected as the primary implementation dataset; final experimental freeze is conditional on local verification of access terms, decoding, labels, audio-video pairing, storage, metadata and leakage-resistant splits.

Raw dataset files are never committed to this repository.

See:
- docs/research/DATASET_SELECTION.md
- docs/requirements/SRS.md
- docs/requirements/SRS_TRACEABILITY.md
- docs/research/RESEARCH_PLAN.md
- docs/research/RISK_AND_VALIDITY_PROTOCOL.md

## Research Questions

1. How much does audio contribute beyond a visual baseline?
2. How much does visual evidence contribute beyond an audio baseline?
3. Does simple multimodal fusion improve over unimodal systems?
4. Does reliability-aware temporal fusion provide measurable additional value?
5. Can temporal evidence localize manipulated intervals where labels permit?
6. How does the model behave when audio and visual evidence disagree?
7. How robust is the system to modality degradation and distribution shift?

## Experimental Ladder

1. Dataset and split validation
2. Video-only baseline
3. Audio-only baseline
4. Simple score/feature fusion
5. Proposed reliability-aware temporal fusion
6. Ablation studies
7. Cross-manipulation/distribution evaluation
8. Robustness evaluation
9. Modality disagreement and error analysis
10. Reproducibility and paper package

## Proposed Architecture

Video -> visual preprocessing -> visual encoder -> temporal features
Audio -> audio preprocessing -> acoustic encoder -> temporal features
Both -> temporal alignment -> cross-modal interaction -> reliability estimation -> dynamic modality weighting -> temporal fusion -> segment/video prediction

The proposed model will be compared against strong unimodal and transparent fusion baselines.

## Engineering Requirements

- persistent dataset manifests;
- chunked and resumable preprocessing;
- configurable sampling and segment sizes;
- explicit train/validation/test splits;
- identity/source leakage checks where metadata permits;
- experiment IDs, seeds, configs and code/model versions;
- raw-data and secret exclusions;
- shared preprocessing between evaluation and inference.

## Repository and Data Structure

The repository contains code, documentation, experiment definitions and reproducibility metadata. The large LAV-DF media files remain outside GitHub.

```
multimodal-deepfake-detection/
├── data/
│   ├── metadata/
│   ├── manifests/
│   ├── splits/
│   ├── cache/
│   ├── checkpoints/
│   └── logs/
├── features/
│   ├── audio/
│   └── visual/
├── docs/
│   ├── requirements/
│   ├── research/
│   └── uml/
├── src/
├── tests/
├── experiments/
├── notebooks/
├── configs/
├── scripts/
├── results/
└── README.md
```

### Local / Google Drive raw-data layout

The downloaded LAV-DF dataset is approximately 25 GB and should be stored under:

```
data/raw/LAV-DF/
├── train/
├── dev/
└── test/
```

For Google Colab, the persistent copy should be under the corresponding `data/raw/LAV-DF` path in Google Drive. The raw media is never committed to GitHub.

See **[docs/research/DATA_LAYOUT.md](docs/research/DATA_LAYOUT.md)** for the storage, manifest, chunking and checkpoint policy.

## Development Milestones

- M0: definition, requirements and architecture
- M1: LAV-DF verification and restart-safe preprocessing
- M2: visual baseline
- M3: audio baseline
- M4: simple multimodal baseline
- M5: proposed reliability-aware temporal fusion
- M6: optimization and experiment infrastructure
- M7: ablation, generalization and robustness
- M8: explainability and error analysis
- M9: inference/demo
- M10: reproducibility package and research paper

## Research Integrity

Accuracy alone is not treated as proof of a successful detector. The project explicitly addresses data leakage, identity/source leakage, manipulation-specific artifacts, class imbalance, calibration, missing modalities, distribution shift and preprocessing/inference mismatch.

The paper will report the evidence actually obtained and will not claim universal generalization or state-of-the-art performance without a fair, current and directly comparable benchmark.

## Current Status

**M1 — Dataset Verification & Preprocessing Pilot**

Next implementation step: build the restart-safe LAV-DF manifest/index and chunked preprocessing pipeline before training the first baseline.
