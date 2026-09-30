# Software Requirements Specification (SRS)

## Project
Robust Multimodal Audio-Visual Deepfake Detection with Reliability-Aware Temporal Fusion and Cross-Manipulation Generalization

Document status: Research baseline SRS — updated 2026-09-30
Primary dataset: LAV-DF (Localized Audio-Visual DeepFake Dataset), subject to final local verification/freeze

## 1. Purpose
This SRS defines the complete software, machine-learning, research, evaluation, reproducibility, security, and deployment requirements for the audio-visual deepfake detection system.

## 2. Problem Definition
The system shall determine whether multimedia content is authentic or manipulated using visual, acoustic, multimodal, and temporal evidence. The research investigates whether reliability-aware temporal audio-visual fusion improves robustness compared with unimodal and simple-fusion baselines.

Proposed research additions:
- Temporal localization: estimate authenticity evidence over temporal segments where labels permit.
- Reliability-aware fusion: estimate modality reliability per temporal segment and dynamically weight audio and visual evidence.
- Modality disagreement analysis: explicitly study cases where audio and video provide conflicting signals.

These additions are research hypotheses and must be experimentally validated.

## 3. Scope
### In scope
- Video/audio ingestion and validation
- Dataset indexing, metadata and split management
- Restart-safe chunked preprocessing
- Frame/face and audio preprocessing
- Temporal segmentation and synchronization
- Visual and acoustic feature extraction
- Visual-only and audio-only baselines
- Simple multimodal fusion
- Reliability-aware temporal fusion
- Classification and temporal scoring
- Ablation, robustness and cross-manipulation evaluation
- Error analysis, calibration and explainability
- Experiment tracking and reproducible inference
- Lightweight demonstration application

### Out of scope
- Committing or redistributing raw datasets
- Claiming universal real-world deepfake detection
- Treating confidence as factual proof
- Using test data for model selection
- Production forensic certification

## 4. Stakeholders
- Student/research developer
- Project supervisor/faculty reviewer
- Research/conference evaluator
- End user of the demonstration application
- Future researchers reproducing or extending the experiments

## 5. Inputs
- Video files
- Associated audio tracks
- Dataset labels and metadata
- Dataset split/identity/source metadata where available
- Experiment and model configuration
- Optional inference-time media

## 6. Outputs
Required: REAL/DEEPFAKE classification, model score, visual score, audio score, fused score, evaluation metrics, confusion matrix and experiment metadata.

Research outputs: temporal segment scores, suspicious intervals where supported, modality reliability weights, disagreement indicators, calibration metrics, robustness results, ablation results and error-analysis records.

## 7. Functional Requirements
- FR-01 Input validation: validate format, readability, duration, frames and audio.
- FR-02 Dataset indexing: create a lightweight manifest containing sample IDs, logical paths, labels, metadata, split and preprocessing status.
- FR-03 Restart-safe processing: process in chunks and persist progress so completed samples are not recomputed after a runtime restart.
- FR-04 Data integrity: detect missing, corrupt, unreadable and duplicate/near-duplicate samples where practical.
- FR-05 Split management: maintain explicit train/validation/test splits and support identity/source grouping.
- FR-06 Visual preprocessing: configurable frame sampling and face/region processing.
- FR-07 Audio preprocessing: configurable extraction, validation, resampling and acoustic representation.
- FR-08 Temporal segmentation: configurable synchronized temporal windows.
- FR-09 Visual baseline: train and evaluate a visual-only detector.
- FR-10 Audio baseline: train and evaluate an audio-only detector.
- FR-11 Simple multimodal baseline: support transparent score-level or feature-level fusion.
- FR-12 Proposed temporal fusion: fuse visual and acoustic representations over time.
- FR-13 Reliability estimation: estimate modality reliability per temporal segment or equivalent model unit.
- FR-14 Dynamic weighting: weight available modality evidence using learned reliability signals.
- FR-15 Missing-modality handling: detect unavailable/corrupt modalities and apply a documented fallback.
- FR-16 Temporal prediction: produce segment-level scores where protocol permits and aggregate to sample level.
- FR-17 Final prediction: output REAL/DEEPFAKE and an associated model score.
- FR-18 Evaluation: calculate accuracy, precision, recall, F1, ROC-AUC and confusion matrices.
- FR-19 Additional evaluation: support PR-AUC, EER where appropriate, calibration, per-condition metrics, latency and resource usage.
- FR-20 Cross-manipulation evaluation: support shifted manipulation/distribution protocols where valid.
- FR-21 Robustness evaluation: support compression, reduced resolution, audio degradation and temporal sampling perturbations.
- FR-22 Ablation: remove/simplify reliability weighting, temporal modeling, cross-modal interaction and other proposed components.
- FR-23 Modality disagreement: identify and record materially conflicting modality predictions.
- FR-24 Error analysis: support false-positive, false-negative, class-wise, condition-wise and modality-specific analysis.
- FR-25 Explainability: provide technically supported temporal, modality and attribution evidence.
- FR-26 Experiment logging: record configuration, dataset/split, code/model version, seed, metrics and artifact identifiers.
- FR-27 Reproducible inference: use the versioned preprocessing required by the corresponding evaluation.
- FR-28 Demo: optionally accept a video and display classification, score, temporal evidence and modality information.

## 8. Non-Functional Requirements
- NFR-01 Reproducibility: document dependencies, configurations, seeds, splits and dataset versions.
- NFR-02 Modularity: audio, visual, temporal, fusion, evaluation and inference components are independently replaceable where practical.
- NFR-03 Scalability: support chunking, batching, caching and resumable execution.
- NFR-04 Colab compatibility: persist manifests/checkpoints externally so kernel restarts do not erase progress.
- NFR-05 Performance: sampling rate, resolution, batch size, segment duration and feature dimensions are configurable.
- NFR-06 Maintainability: critical utilities have tests and clear interfaces.
- NFR-07 Auditability: trace results to configuration, split, manifest and code/model version.
- NFR-08 Security: never commit credentials or secrets.
- NFR-09 Data safety: raw dataset media is never committed to GitHub.
- NFR-10 Fault tolerance: a failed sample should be logged without terminating the complete job where feasible.
- NFR-11 Determinism: seeds and deterministic settings are configurable and recorded.
- NFR-12 Resource awareness: major experiments record hardware and resource usage where feasible.

## 9. Dataset Requirements
The primary dataset is LAV-DF. It is selected for the current implementation because it is specifically audio-visual and provides real/manipulated samples suitable for visual, audio and multimodal experiments.

Status: Primary dataset selected; final experimental freeze remains conditional on local verification.

Before freeze, verify access terms, download, decoding, audio-video pairing, labels, metadata, manipulation categories, class distribution, duplicate/near-duplicate risk, identity/source leakage and storage/preprocessing feasibility.

Raw LAV-DF media shall not be committed to GitHub. The repository may contain dataset documentation, access instructions, schemas, non-sensitive manifests, preprocessing code, split definitions, configurations and lightweight results.

## 10. Research Requirements
- Establish visual-only, audio-only and simple-fusion baselines before the proposed model.
- Evaluate reliability-aware temporal fusion against these baselines.
- Perform ablations for each major proposed component.
- Perform cross-manipulation/distribution evaluation where a defensible protocol exists.
- Perform selected robustness experiments.
- Analyze modality disagreement and missing-modality behavior.
- Use multiple seeds and uncertainty reporting for important experiments when compute permits.
- Measure calibration if confidence is exposed to users.
- Keep failed or inconclusive experiments traceable.

## 11. Evaluation Requirements
Primary metrics: ROC-AUC, F1, precision, recall and accuracy.

Secondary metrics where appropriate: PR-AUC, EER, calibration metrics, confusion matrix, per-class/per-manipulation/per-condition metrics, inference latency and memory/resource usage.

Required comparison ladder:
1. Visual-only baseline
2. Audio-only baseline
3. Simple fusion
4. Proposed reliability-aware temporal fusion
5. Proposed minus reliability weighting
6. Proposed minus temporal module
7. Proposed minus cross-modal interaction
8. Cross-manipulation evaluation
9. Robustness evaluation

## 12. Data Leakage and Validity
The system shall prevent test-set influence on model selection, investigate identity/source leakage and duplicates, document manipulation categories and class distributions, prevent train/test preprocessing leakage, and maintain fixed evaluation definitions.

A high accuracy score alone shall not constitute research validation.

## 13. Explainability
The system may expose visual contribution, audio contribution, temporal suspiciousness, modality reliability, disagreement and attribution maps. Such outputs are model-derived evidence, not proof that a highlighted region is objectively manipulated.

## 14. Experiment Artifacts
Each experiment should record:
- experiment ID
- dataset/version
- split ID
- model version
- code commit
- configuration
- random seed
- hardware
- training duration
- checkpoint identifier
- metrics
- evaluation protocol
- notes.

Large checkpoints and raw media should use external storage rather than Git history.

## 15. Architecture
Data Layer -> Manifest/Validation
Preprocessing Layer -> Video/Face + Audio + Temporal Synchronization
Feature Layer -> Visual Encoder + Audio Encoder
Model Layer -> Visual Baseline + Audio Baseline + Simple Fusion + Proposed Reliability-Aware Temporal Fusion
Evaluation Layer -> Metrics + Ablation + Robustness + Generalization + Error Analysis
Explainability Layer -> Temporal Evidence + Modality Reliability + Attribution
Experiment Layer -> Configurations + Checkpoints + Logs + Results
Application Layer -> Reproducible Inference/Demo

## 16. Development Milestones
- M0 Definition: requirements, scope, research questions, UML and architecture.
- M1 Dataset verification/preprocessing: LAV-DF access, metadata, manifest, integrity and resumable processing.
- M2 Visual baseline.
- M3 Audio baseline.
- M4 Simple multimodal baseline.
- M5 Proposed temporal reliability-aware fusion.
- M6 Optimization and experiment infrastructure.
- M7 Ablation, cross-manipulation, robustness and disagreement studies.
- M8 Explainability and error analysis.
- M9 Inference application/demo.
- M10 Reproducibility package and research paper.

## 17. Acceptance Criteria
- LAV-DF access and terms documented.
- Dataset structure and audio/video pairing verified.
- Dataset manifest generated.
- Processing is restart-safe.
- Visual, audio and simple-fusion baselines are reproducible.
- Proposed fusion is implemented and evaluated.
- Reliability and temporal ablations are completed.
- Generalization/robustness experiments are completed where supported.
- Modality disagreement and error analysis are documented.
- Primary/secondary metrics are reported.
- Test data remains isolated from model selection.
- Experiments are traceable to code/configuration/split.
- Raw dataset files are excluded from GitHub.
- Limitations and threats to validity are documented.
- Final claims do not exceed the evidence.

## 18. Ethical, Legal and Research Integrity
The system shall not be presented as a definitive forensic authority. Dataset licenses and access terms shall be respected. Restricted media shall not be redistributed. Results shall distinguish experimental evidence from certainty, disclose limitations, avoid selective reporting, and avoid unsupported claims of universal generalization or state-of-the-art performance.

## 19. Current Status
Milestone: M1 — Dataset Verification & Preprocessing Pilot.
Primary dataset: LAV-DF.
Research focus: multimodal audio-visual detection.
Proposed addition: reliability-aware temporal fusion.
Additional outputs: temporal localization, modality disagreement, robustness, ablation and explainability.
Raw dataset policy: never commit to GitHub.
Next implementation task: restart-safe LAV-DF indexing and chunked preprocessing.