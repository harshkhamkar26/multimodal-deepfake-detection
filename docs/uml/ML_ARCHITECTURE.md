# UML-07 — ML Architecture Specification

## Objective

Define the learning architecture at a level that can be implemented, tested, and revised after dataset/compute validation.

## Proposed Research Architecture

```text
                           VIDEO
                             │
                 ┌───────────┴───────────┐
                 │                       │
                 ▼                       ▼
          Frame Sampling            Audio Extraction
                 │                       │
                 ▼                       ▼
          Face/Region Prep       Segment / Resample
                 │                       │
                 ▼                       ▼
          Visual Encoder         Acoustic Encoder
                 │                       │
                 ▼                       ▼
          Temporal Features      Temporal Features
                 │                       │
                 └───────────┬───────────┘
                             ▼
                     Multimodal Fusion
                             │
                             ▼
                       Classifier Head
                             │
                 ┌───────────┴───────────┐
                 ▼                       ▼
             REAL/FAKE             Authenticity Score
                                         │
                                  Calibration/Evaluation
```

## Branch Responsibilities

### Visual branch

1. Decode/sample frames.
2. Apply reproducible spatial preprocessing.
3. Extract visual representations with a selected encoder.
4. Aggregate information across time.
5. Expose a visual-only prediction for baseline evaluation.

### Audio branch

1. Extract the audio track when available.
2. Apply reproducible resampling/segmentation.
3. Transform the signal into the selected acoustic representation.
4. Extract acoustic representations with a selected encoder.
5. Aggregate information across time.
6. Expose an audio-only prediction for baseline evaluation.

### Fusion branch

The architecture must permit comparison of at least:

- score-level/simple fusion baseline;
- feature-level fusion baseline;
- proposed learned fusion mechanism.

The exact proposed fusion method remains a decision after dataset and compute assessment.

## Training Modes

The implementation should support:

- frozen pretrained encoders + trainable heads;
- partial fine-tuning;
- end-to-end fine-tuning when compute and data justify it.

## Required Experimental Models

| Model | Role |
|---|---|
| Video-only | Visual baseline |
| Audio-only | Audio baseline |
| Simple fusion | Transparent multimodal baseline |
| Proposed fusion | Research model |
| Proposed fusion ablations | Contribution analysis |

## Key Architectural Constraints

- Both modality branches must be independently testable.
- Fusion must not hide modality-specific failures.
- The same test protocol must be used when comparing models.
- Temporal information must not be discarded without an explicit baseline justification.
- Exact encoders are not frozen until dataset and compute audits are complete.

## Research Hypothesis

The working hypothesis is that complementary audio-visual evidence can improve robustness under selected distribution shifts compared with unimodal and naive-fusion baselines. This remains experimentally testable and must not be presented as a guaranteed result.
