# SRS Traceability Matrix

This document maps the SRS requirements to implementation milestones and research evidence.

| Requirement area | Planned implementation | Verification/evidence |
|---|---|---|
| Input validation | Dataset/media validation utilities | Validation logs and tests |
| Dataset indexing | Persistent manifest generator | Manifest + sample counts |
| Restart-safe processing | Chunk checkpoints and status fields | Resume test after runtime restart |
| Visual pipeline | Video/frame/face preprocessing + visual encoder | Visual baseline metrics |
| Audio pipeline | Audio extraction/representation + acoustic encoder | Audio baseline metrics |
| Temporal segmentation | Shared segment timeline | Alignment audit |
| Simple fusion | Score/feature fusion baseline | Baseline comparison |
| Reliability estimation | Learned modality reliability module | Reliability ablation |
| Dynamic fusion | Reliability-weighted temporal fusion | Proposed-model evaluation |
| Missing modality | Explicit fallback policy | Missing-modality experiment |
| Temporal prediction | Segment-level scoring | Localization/error analysis |
| Evaluation | Central metrics module | Reproducible metric tables |
| Cross-manipulation | Controlled shifted-condition split | Generalization results |
| Robustness | Configurable perturbation pipeline | Robustness tables |
| Modality disagreement | Audio/video score comparison | Disagreement analysis |
| Explainability | Temporal/modality evidence outputs | Explanation examples + limitations |
| Experiment logging | Config/seed/commit/checkpoint metadata | Experiment registry |
| Reproducibility | Pinned dependencies and configs | Re-run protocol |
| Security | Secrets/data exclusions | Repository audit |
| Demo | Reproducible inference interface | End-to-end inference test |

## Research acceptance gates

- Gate 1: SRS and architecture updated.
- Gate 2: LAV-DF access and pilot verified.
- Gate 3: Manifest and resumable preprocessing validated.
- Gate 4: Visual/audio baselines completed.
- Gate 5: Simple fusion completed.
- Gate 6: Reliability-aware temporal model implemented.
- Gate 7: Ablations completed.
- Gate 8: Generalization/robustness/disagreement analysis completed where supported.
- Gate 9: Final test protocol frozen and evaluated.
- Gate 10: Paper figures, tables, limitations and reproducibility package completed.

## Data governance

Raw LAV-DF media, generated caches and large model artifacts must remain outside Git history unless their license and repository policy explicitly permit otherwise. GitHub stores code, documentation, configurations, lightweight metadata and research summaries.
