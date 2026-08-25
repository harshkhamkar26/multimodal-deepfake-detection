# M0 — Project Scope and Requirements

## Project Title

**Robust Multimodal Audio-Visual Deepfake Detection with Cross-Manipulation Generalization**

## 1. Problem Statement

Deepfake generation systems can manipulate visual content, speech/audio, or both. Detectors trained and evaluated under narrowly matched data distributions may report strong in-distribution performance while degrading when the manipulation method, compression, identity, or modality conditions change.

This project will develop and evaluate a multimodal detector that combines visual and acoustic evidence and explicitly measures whether multimodal learning improves robustness beyond unimodal baselines.

## 2. Primary Objective

Design, implement, and experimentally evaluate a reproducible audio-visual deepfake detection pipeline that:

- analyzes visual and audio evidence independently;
- establishes strong unimodal baselines;
- compares simple and proposed multimodal fusion;
- evaluates generalization under changed manipulation conditions;
- studies modality disagreement and failure cases; and
- produces auditable inference outputs and research documentation.

## 3. Secondary Objectives

- Keep the system modular enough to replace individual encoders or fusion strategies.
- Make experiments reproducible through configuration and version control.
- Quantify performance using multiple metrics rather than accuracy alone.
- Document limitations and threats to validity.
- Provide a practical inference/demo layer after the research evaluation is stable.

## 4. In Scope

- Video authenticity analysis
- Audio authenticity analysis
- Audio-visual feature fusion
- Identity-aware data splitting
- In-distribution evaluation
- Cross-manipulation evaluation where supported by the selected dataset
- Ablation studies
- Modality-disagreement analysis
- Robustness/error analysis
- Explainability appropriate to the selected models
- Reproducible experiment tracking
- Local inference/demo application

## 5. Out of Scope

- Creating or distributing deepfake-generation tooling
- Claiming universal detection of all synthetic media
- Treating a single public dataset as proof of real-world generalization
- Committing raw datasets or large model checkpoints to Git
- Optimizing for a single headline accuracy number at the expense of valid evaluation

## 6. Functional Requirements

### FR-01 — Video Input
The system shall accept a supported video file and validate its format, duration, frame availability, and audio availability where applicable.

### FR-02 — Visual Processing
The system shall sample/process video frames and generate visual representations suitable for authenticity classification.

### FR-03 — Audio Processing
The system shall extract available audio and generate acoustic representations suitable for authenticity classification.

### FR-04 — Unimodal Inference
The system shall support independent visual-only and audio-only inference for baseline evaluation and diagnostics.

### FR-05 — Multimodal Fusion
The system shall combine audio and visual evidence through a defined fusion mechanism.

### FR-06 — Prediction
The system shall output an authenticity class and an associated model confidence/probability, subject to calibration and threshold analysis.

### FR-07 — Evidence
The system should provide modality-level and/or region/frame-level evidence where supported by the model and explainability method.

### FR-08 — Experiment Reproducibility
Training and evaluation shall be configurable through version-controlled configuration files and deterministic settings where technically possible.

### FR-09 — Evaluation
The pipeline shall calculate accuracy, precision, recall, F1-score, ROC-AUC and confusion matrices where applicable.

### FR-10 — Generalization Evaluation
The evaluation framework shall support testing under manipulation or distribution conditions different from the training condition when the selected data supports this design.

## 7. Non-Functional Requirements

### NFR-01 — Reproducibility
A documented environment and configuration shall allow another developer to reproduce the principal experiments.

### NFR-02 — Modularity
Audio, video, fusion, training, evaluation and explainability components shall have clear interfaces.

### NFR-03 — Maintainability
Code shall follow a consistent package structure, type/documentation conventions where appropriate, and automated tests for critical utilities.

### NFR-04 — Security
Secrets and credentials shall never be committed. Uploaded media shall be treated as untrusted input.

### NFR-05 — Resource Awareness
The system shall be designed to support constrained research hardware through configurable frame sampling, batch size, resolution, model size and caching.

### NFR-06 — Auditability
Experiments shall record dataset version/split, configuration, model version, metrics and relevant random seeds.

## 8. Success Criteria

The project will be considered successful when it has:

1. reproducible audio and visual preprocessing;
2. credible video-only and audio-only baselines;
3. a reproducible multimodal baseline;
4. a clearly motivated proposed fusion approach;
5. controlled ablation experiments;
6. a defensible generalization experiment;
7. complete metric reporting and error analysis; and
8. documentation sufficient for technical review and paper preparation.

A high accuracy result is desirable, but **scientific validity and generalization are primary acceptance criteria**.

## 9. Research Contribution Hypothesis

The working hypothesis is that a carefully designed multimodal detector can exploit complementary audio and visual authenticity cues and achieve better robustness under selected distribution shifts than unimodal or naive-fusion baselines. This is a hypothesis to test, not a result assumed in advance.
