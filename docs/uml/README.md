# UML & System Design

## Purpose

This directory defines the software/system design for the Multimodal Deepfake Detection project. The UML artifacts are derived from the approved project scope and research plan and will be kept consistent with the implementation.

## Design Principle

The system is treated as a research-grade, modular ML system with separate data ingestion, visual analysis, audio analysis, fusion, evaluation, explainability, and presentation/deployment concerns.

## UML Deliverables

| ID | Artifact | Purpose | Status |
|---|---|---|---|
| UML-01 | System Context Diagram | Defines external actors/systems and system boundary | Planned |
| UML-02 | Use Case Diagram | Defines user and system interactions | Planned |
| UML-03 | Activity Diagram | Defines end-to-end processing workflow | Planned |
| UML-04 | Sequence Diagram | Defines runtime interaction between major components | Planned |
| UML-05 | Component Diagram | Defines software/module boundaries and dependencies | Planned |
| UML-06 | Deployment Diagram | Defines execution/deployment topology | Planned |
| UML-07 | ML Architecture Diagram | Defines visual, audio and fusion learning paths | Planned |
| UML-08 | Data Flow Diagram | Defines movement and transformation of media/data | Planned |
| UML-09 | Experiment Architecture | Defines baseline, fusion, ablation and generalization evaluation | Planned |

## System Boundary

The proposed system begins when a user or evaluation pipeline provides a supported video and ends with an authenticity decision and associated evidence. Training and research evaluation are separate workflows from end-user inference, although they share preprocessing and model components.

### Primary external actors

- **End User:** submits a video and consumes the inference result.
- **Researcher/Developer:** configures experiments, trains models, evaluates results, and inspects failures.
- **Dataset Source:** provides authorized research media and metadata.
- **Model/Artifact Store:** provides versioned model artifacts during inference/training.

### Major internal subsystems

1. Input & Validation
2. Media Preprocessing
3. Visual Analysis Pipeline
4. Audio Analysis Pipeline
5. Multimodal Fusion
6. Prediction & Calibration
7. Explainability/Evidence
8. Experiment & Evaluation Engine
9. Persistence/Results
10. Presentation/API Layer

## Core Inference Flow

```text
Video Input
    |
    v
Validation & Media Inspection
    |
    +--------------------+
    |                    |
    v                    v
Video Preprocessing   Audio Extraction
    |                    |
    v                    v
Visual Encoder       Audio Encoder
    |                    |
    +---------+----------+
              |
              v
        Fusion Module
              |
              v
      Prediction / Score
              |
       +------+------+
       |             |
       v             v
  Calibration    Explainability
       |             |
       +------+------+
              |
              v
     Final Inference Result
```

## Research/Evaluation Flow

```text
Dataset Audit
     |
     v
Leakage-resistant Split
     |
     +----------------+----------------+
     |                |                |
     v                v                v
Video Baseline    Audio Baseline   Simple Fusion
     |                |                |
     +----------------+----------------+
                      |
                      v
               Proposed Fusion
                      |
             +--------+--------+
             |                 |
             v                 v
          Ablation      Cross-Manipulation
             |            / Distribution
             |                Shift
             +--------+--------+
                      |
                      v
               Error Analysis
                      |
                      v
              Final Conclusions
```

## Design Constraints

- Raw datasets and large model artifacts are not stored in Git.
- Training/evaluation data must be separated from test data.
- Identity/source leakage must be assessed where metadata permits.
- Audio and video branches must remain independently testable.
- The fusion layer must be replaceable so that multiple fusion strategies can be compared fairly.
- Explainability output must be described as model attribution/evidence, not as ground-truth proof of manipulation.
- Deployment is downstream of research validation.

## Decision Gate

The UML design is considered ready for implementation only when each diagram answers a distinct architectural question and the diagrams are mutually consistent with the requirements and research plan.
