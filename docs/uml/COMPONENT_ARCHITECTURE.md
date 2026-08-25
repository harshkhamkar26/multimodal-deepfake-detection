# UML-05 — Component Architecture

## 1. Objective

Define the logical software components and their responsibilities before implementation.

## 2. High-Level Component Model

```text
┌──────────────────────────────────────────────────────────────┐
│                    Presentation Layer                        │
│                  Web UI / REST API                           │
└────────────────────────────┬─────────────────────────────────┘
                             │
                             ▼
┌──────────────────────────────────────────────────────────────┐
│                  Inference Orchestrator                      │
│       request validation • pipeline coordination             │
└───────────────┬──────────────────────────────┬───────────────┘
                │                              │
                ▼                              ▼
┌───────────────────────────┐      ┌───────────────────────────┐
│      Video Pipeline       │      │       Audio Pipeline      │
│ frame sampling            │      │ audio extraction          │
│ face/region processing    │      │ resampling/segmentation   │
│ visual encoder            │      │ acoustic representation   │
│ temporal aggregation      │      │ audio encoder             │
└──────────────┬────────────┘      └──────────────┬────────────┘
               │                                  │
               └────────────────┬─────────────────┘
                                ▼
                    ┌────────────────────────┐
                    │    Fusion Component    │
                    │ feature/score fusion   │
                    └────────────┬───────────┘
                                 ▼
                    ┌────────────────────────┐
                    │ Prediction Component   │
                    │ classifier + threshold │
                    └────────────┬───────────┘
                                 │
                    ┌────────────┴────────────┐
                    ▼                         ▼
          ┌──────────────────┐       ┌──────────────────┐
          │ Calibration      │       │ Explainability   │
          │ evaluation       │       │ visual/audio    │
          └────────┬─────────┘       └────────┬─────────┘
                   └────────────┬─────────────┘
                                ▼
                    ┌────────────────────────┐
                    │ Result / Report Layer  │
                    └────────────────────────┘

Research plane (separate from serving):

Dataset Manager → Preprocessing → Experiment Runner
                                  ├→ Video Trainer
                                  ├→ Audio Trainer
                                  ├→ Fusion Trainer
                                  └→ Evaluation / Metrics → Results
```

## 3. Component Responsibilities

### Presentation Layer
Handles user interaction and/or API contracts. It must not contain model-training logic.

### Inference Orchestrator
Coordinates validation, preprocessing, modality execution, fusion, prediction, evidence generation, and result assembly.

### Video Pipeline
Owns frame sampling, visual preprocessing, visual representation learning, and temporal aggregation.

### Audio Pipeline
Owns audio extraction, segmentation/resampling, acoustic representation, and audio representation learning.

### Fusion Component
Consumes independently testable visual and audio representations or scores and produces a multimodal representation/score.

### Prediction Component
Maps the fused representation to an authenticity score/class and exposes thresholding as an explicit configuration rather than hard-coded application logic.

### Calibration Component
Evaluates or applies calibration procedures when the project claims calibrated confidence. It is not synonymous with the classifier's raw softmax output.

### Explainability Component
Generates model-attribution evidence appropriate to the selected architecture. It must retain the model/version and input context associated with the explanation.

### Result/Report Layer
Converts model outputs and evidence into a stable response/report schema.

### Dataset Manager
Maintains dataset manifests, metadata references, split definitions, and validation checks without storing raw datasets in Git.

### Experiment Runner
Orchestrates reproducible training/evaluation configurations and records experiment metadata.

### Evaluation/Metrics
Calculates agreed metrics and produces comparable summaries for baselines, fusion, ablation, robustness, and generalization experiments.

## 4. Dependency Rules

1. Presentation depends on inference contracts, not internal model implementations.
2. Inference orchestration may depend on modality pipelines, fusion, prediction, calibration, and explainability interfaces.
3. Video and audio pipelines must remain independently executable for baseline evaluation.
4. Fusion must not directly own raw media extraction.
5. Research training code must not be required by production inference.
6. Evaluation must consume versioned predictions/configuration and must not silently alter test data.

## 5. Architecture Decision Pending

Exact encoder classes, feature dimensions, fusion algorithm, API framework, and storage implementation remain open until dataset and compute assessment are completed.
