# UML-02 — Use Case Specification

## 1. Actors

### End User
Uses the deployed application to submit a supported video and inspect the detection result.

### Researcher / Developer
Uses the research pipeline to prepare data, configure experiments, train models, evaluate models, inspect failures, and manage experiment artifacts.

### Dataset Source
Provides authorized media and metadata for research workflows.

### Model / Artifact Store
Provides versioned trained model artifacts to inference/evaluation components.

## 2. End-User Use Cases

### UC-01 — Submit Video
**Actor:** End User

The user selects or uploads a supported video.

**Preconditions:** Application is available and input format is supported.

**Postconditions:** A validated media object is passed to the inference pipeline or a validation error is returned.

### UC-02 — Validate Media
**Actor:** System

Checks file accessibility, supported format, duration/size constraints, frame availability, and audio availability when required.

### UC-03 — Run Deepfake Detection
**Actor:** End User

The system preprocesses the media, executes the visual and audio branches, performs fusion, and generates an authenticity score/class.

### UC-04 — View Result
**Actor:** End User

Displays the predicted class, score/confidence representation, and processing status.

### UC-05 — Inspect Evidence
**Actor:** End User

Displays supported frame/region/audio/modality evidence associated with the model prediction. Evidence is explicitly presented as model attribution rather than ground-truth proof.

## 3. Researcher Use Cases

### UC-06 — Audit Dataset
Inspect dataset structure, metadata, identities/sources where available, class distribution, duplicates/near-duplicates, modality availability, and leakage risks.

### UC-07 — Define Data Split
Create a reproducible train/validation/test protocol that prevents avoidable source or identity leakage.

### UC-08 — Configure Experiment
Select dataset version, preprocessing configuration, model configuration, seed, training parameters, and evaluation protocol.

### UC-09 — Train Video Baseline
Train/evaluate a visual-only detector.

### UC-10 — Train Audio Baseline
Train/evaluate an audio-only detector.

### UC-11 — Train Simple Fusion Baseline
Combine modality representations or scores using a transparent baseline fusion strategy.

### UC-12 — Train Proposed Fusion
Train the proposed multimodal fusion architecture after the baseline evidence and architecture decision gate are satisfied.

### UC-13 — Run Ablation
Remove or alter proposed components to measure their individual contribution.

### UC-14 — Run Generalization Evaluation
Evaluate under a defined cross-manipulation or distribution-shift protocol supported by the selected data.

### UC-15 — Run Robustness Evaluation
Evaluate selected changes such as compression, resolution, audio quality, or temporal sampling where feasible.

### UC-16 — Analyze Errors
Inspect false positives, false negatives, modality disagreement, calibration behavior, and condition-specific performance.

### UC-17 — Manage Model Artifacts
Version, register, load, and document model artifacts without committing large binary artifacts into source control.

### UC-18 — Generate Research Results
Produce reproducible metrics, tables, plots, and experiment summaries for comparison and paper preparation.

## 4. Relationships

```text
END USER
  |
  +--> UC-01 Submit Video
  |       |
  |       +--> UC-02 Validate Media
  |       |
  |       +--> UC-03 Run Detection
  |                |
  |                +--> UC-04 View Result
  |                |
  |                +--> UC-05 Inspect Evidence
  |
RESEARCHER / DEVELOPER
  |
  +--> UC-06 Audit Dataset
  +--> UC-07 Define Data Split
  +--> UC-08 Configure Experiment
  +--> UC-09 Train Video Baseline
  +--> UC-10 Train Audio Baseline
  +--> UC-11 Train Simple Fusion
  +--> UC-12 Train Proposed Fusion
  |        |
  |        +--> UC-13 Run Ablation
  |        +--> UC-14 Generalization Evaluation
  |        +--> UC-15 Robustness Evaluation
  |        +--> UC-16 Analyze Errors
  +--> UC-17 Manage Model Artifacts
  +--> UC-18 Generate Research Results

DATASET SOURCE --> UC-06 Audit Dataset
MODEL/ARTIFACT STORE --> UC-17 Manage Model Artifacts
