# UML-07 — ML Architecture Specification

## Objective

Define an implementable multimodal architecture for the LAV-DF research pipeline while preserving strong unimodal and simple-fusion baselines.

## Proposed Research Architecture

```
VIDEO -----------------------> Frame/Face Preprocessing ---> Visual Encoder ---                                                                                                                                                                 -> Temporal Alignment
                                                                                       |
AUDIO ----------------------> Audio Preprocessing ----------> Audio Encoder ----/       |
                                                                                       v
                                                                          Cross-Modal Interaction
                                                                                       |
                                                                                       v
                                                                          Reliability Estimator
                                                                                       |
                                                                                       v
                                                                       Dynamic Modality Weighting
                                                                                       |
                                                                                       v
                                                                            Temporal Fusion Block
                                                                                       |
                                                        +------------------------------+----------------+
                                                        |                                               |
                                                        v                                               v
                                                Segment Scores                                   Video Score
                                                        |                                               |
                                                        +-----------------------+-----------------------+
                                                                                |
                                                                                v
                                                                      Calibration / Explainability
```

## Branch Responsibilities

### Visual branch
1. Decode and sample frames.
2. Apply reproducible spatial/face preprocessing.
3. Extract visual representations.
4. Preserve temporal ordering.
5. Produce visual-only predictions for the baseline.

### Audio branch
1. Extract and validate audio.
2. Resample and segment reproducibly.
3. Generate the selected acoustic representation.
4. Extract acoustic representations.
5. Preserve temporal alignment with visual segments.
6. Produce audio-only predictions for the baseline.

### Temporal alignment
Audio and visual features shall be mapped to a common segment timeline. The alignment strategy and segment duration shall be configurable and recorded.

### Reliability estimator
The proposed model shall estimate a reliability value for each available modality at each temporal segment or equivalent model unit.

Potential reliability signals may include learned feature quality, modality consistency, prediction uncertainty or learned attention. The exact mechanism must be selected through experiments rather than assumed.

### Dynamic fusion
The proposed fusion shall use the reliability signals to weight modality evidence before producing the fused temporal representation.

A missing or unusable modality shall receive a documented fallback treatment rather than silently contributing zero evidence.

## Required Experimental Models

| Model | Role |
|---|---|
| Video-only | Visual baseline |
| Audio-only | Audio baseline |
| Simple score fusion | Transparent multimodal baseline |
| Simple feature fusion | Stronger baseline |
| Proposed temporal fusion | Research model |
| Proposed without reliability | Reliability ablation |
| Proposed without temporal modeling | Temporal ablation |
| Proposed without cross-modal interaction | Fusion ablation |

## Research Outputs

The implementation should expose:
- video-only score;
- audio-only score;
- fused score;
- temporal segment scores;
- modality reliability values;
- modality disagreement;
- confidence/calibration information where supported.

## Training Modes

Support:
- frozen pretrained encoders + trainable heads;
- partial fine-tuning;
- end-to-end fine-tuning when compute and data justify it.

## Engineering Constraints

- Both modality branches must be independently testable.
- Fusion must not hide modality-specific failures.
- Temporal information must be retained unless an experiment explicitly defines a non-temporal baseline.
- Exact encoders are not frozen until the dataset/compute pilot is complete.
- Preprocessing must be shared between evaluation and inference.
- Chunked feature extraction must be resumable after runtime restart.

## Research Hypothesis

Reliability-aware temporal fusion may improve robustness when one modality is less informative, degraded or inconsistent with the other modality. This is an experimentally testable hypothesis, not a guaranteed result.
