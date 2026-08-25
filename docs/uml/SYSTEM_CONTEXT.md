# UML-01 — System Context Specification

## 1. Objective

Define the system boundary and the external actors/systems that interact with the multimodal deepfake detection platform.

## 2. System

**Multimodal Deepfake Detection System**

The system receives supported video media, performs coordinated visual and audio analysis, combines modality evidence, and returns an authenticity assessment with model-supported evidence. It also exposes separate research workflows for training and evaluation.

## 3. External Actors / Systems

### 3.1 End User

Provides a video through the application and receives:

- authenticity prediction;
- prediction score/confidence as supported by calibration;
- visual evidence where supported;
- audio evidence where supported;
- processing/result status.

### 3.2 Researcher / Developer

Interacts with the research pipeline to:

- configure experiments;
- prepare datasets;
- train models;
- compare baselines;
- run ablations;
- run generalization/robustness evaluations;
- inspect errors;
- manage model artifacts and results.

### 3.3 Dataset Source

Supplies authorized research media and metadata used by preprocessing and evaluation. The system does not assume that a dataset is automatically leakage-free; dataset audit is an explicit research activity.

### 3.4 Model / Artifact Store

Stores or supplies versioned trained model artifacts and experiment outputs. Large artifacts are managed outside normal source-code commits.

## 4. System Boundary

### Inside the boundary

- Input validation
- Video/audio extraction
- Visual preprocessing
- Audio preprocessing
- Visual representation and temporal processing
- Audio representation and temporal processing
- Fusion
- Prediction
- Calibration/evaluation logic
- Explainability/evidence generation
- Experiment orchestration
- Result persistence
- API/presentation integration

### Outside the boundary

- Original dataset ownership and collection
- Deepfake generation/manipulation systems
- User identity/authentication systems unless separately introduced
- External cloud storage infrastructure unless selected for deployment

## 5. Context Relationships

```text
                         +----------------------+
                         |   Dataset Source      |
                         +----------+-----------+
                                    |
                              research media
                                    |
                                    v
+-------------+             +-------+-----------------------+             +----------------+
| End User    | -- video -->| Multimodal Deepfake          |<-- artifacts --| Model/Artifact |
|             |<-- result --| Detection System             |                | Store          |
+-------------+             +-------+-----------------------+                +----------------+
                                    ^
                                    |
                         configuration/results
                                    |
                         +----------+-----------+
                         | Researcher/Developer |
                         +----------------------+
```

## 6. Architectural Principle

The end-user inference path and the research/training path share validated preprocessing and model components but remain logically separated. This prevents experimental code from being confused with the production inference contract.

## 7. Open Decisions

These items are intentionally not frozen yet:

- exact web/API framework;
- exact model encoders;
- exact fusion mechanism;
- exact dataset(s);
- local versus cloud deployment;
- final explanation methods per modality.

Those decisions will be made only after the dataset audit, compute assessment, and baseline design.
