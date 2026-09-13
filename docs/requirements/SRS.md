# Software Requirements Specification (SRS)

## Project
**Robust Multimodal Audio-Visual Deepfake Detection with Cross-Manipulation Generalization**

## 1. Purpose

This SRS defines the software requirements for a research-oriented system that detects whether multimedia content is authentic or manipulated using visual, audio, and combined audio-visual evidence.

## 2. Problem Definition

Modern generative AI can create convincing face, speech, and audio-visual manipulations. A detector relying on only one modality can miss evidence available in another modality. The system therefore evaluates visual-only, audio-only, and multimodal detection and studies whether multimodal fusion improves robustness.

## 3. Users and Stakeholders

- Student/research developer
- Project supervisor/faculty reviewer
- Research evaluator
- End user of the final inference/demo application

## 4. System Inputs

- Video files containing visual information
- Audio tracks associated with videos
- Dataset labels/metadata during training and evaluation
- Configuration files controlling preprocessing, training and evaluation

## 5. Functional Requirements

### FR-01: Input Validation
The system shall validate supported media format, readable streams, duration, frame availability, and audio availability.

### FR-02: Visual Pipeline
The system shall sample video frames and produce visual representations for authenticity prediction.

### FR-03: Audio Pipeline
The system shall extract audio and produce acoustic representations for authenticity prediction.

### FR-04: Visual Baseline
The system shall support a visual-only deepfake detector.

### FR-05: Audio Baseline
The system shall support an audio-only deepfake detector.

### FR-06: Multimodal Baseline
The system shall combine visual and audio representations using a reproducible fusion method.

### FR-07: Proposed Fusion
The system shall support experimentation with a motivated multimodal fusion architecture.

### FR-08: Prediction
The system shall produce REAL/DEEPFAKE output and a confidence/probability value.

### FR-09: Evaluation
The system shall report accuracy, precision, recall, F1-score, ROC-AUC and confusion matrices where applicable.

### FR-10: Generalization
Where the selected dataset supports it, the system shall evaluate performance under manipulation or distribution conditions different from training.

### FR-11: Reproducibility
Experiments shall record dataset version, split, configuration, model version and random seed where applicable.

### FR-12: Error Analysis
The system shall support analysis of false positives, false negatives and modality disagreement.

## 6. Non-Functional Requirements

### NFR-01: Reproducibility
The principal experiments shall be repeatable using documented dependencies and configuration.

### NFR-02: Modularity
Audio, visual, fusion, evaluation and inference components shall be independently replaceable where practical.

### NFR-03: Performance
Preprocessing and inference shall use configurable sampling, resolution, batching and caching so the project can operate on constrained research hardware.

### NFR-04: Maintainability
The codebase shall use a clear package structure and tests for critical utilities.

### NFR-05: Security
Credentials and secrets shall not be committed. Input media shall be treated as untrusted data.

### NFR-06: Auditability
Important experiments and results shall be version-controlled and traceable to their configuration and dataset split.

## 7. Dataset Requirements

The primary dataset shall be selected only after verification of:

1. free/open research access or acceptable access terms;
2. video and audio availability;
3. real and manipulated examples;
4. reliable labels/metadata;
5. practical download/storage requirements;
6. suitable diversity for the research questions; and
7. licensing/terms compatible with the academic project.

Raw datasets shall not be committed to GitHub.

## 8. Research Experiments

The minimum experimental sequence is:

1. Visual-only baseline
2. Audio-only baseline
3. Simple multimodal fusion baseline
4. Proposed multimodal fusion
5. Ablation studies
6. Generalization/robustness evaluation
7. Failure and modality-disagreement analysis

## 9. Acceptance Criteria

The software/research implementation is acceptable when the pipeline can reproducibly process the selected dataset, train and evaluate the visual and audio baselines, train and evaluate the multimodal system, produce the defined metrics, and document limitations and failure cases.

A high accuracy number alone is not an acceptance criterion.

## 10. Dataset Status

**Status: Selection under verification.**

The project previously considered gated datasets such as FakeAVCeleb. Current work prioritizes freely accessible candidates. A dataset will be marked FINAL only after access and practical download have been tested.
