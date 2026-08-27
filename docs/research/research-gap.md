# Research Gap

## Problem

Deepfake detectors can report strong benchmark performance while still being vulnerable to distribution shift, dataset shortcuts, unseen manipulation methods, and conflicts between modalities.

## Gaps we will investigate

### Gap 1 — Multimodal evidence is not enough by itself

Audio and video can be fused, but a system that merely concatenates features does not explain whether the modalities agree. We will explicitly model cross-modal consistency as a forensic signal.

### Gap 2 — In-distribution accuracy can hide weak generalization

Random train/test splits may share identities, sources, compression patterns, or manipulation artifacts. We will use identity-aware splits and cross-manipulation/cross-dataset evaluation wherever the selected datasets permit it.

### Gap 3 — Robustness is often secondary

A practical detector must survive common transformations. We will measure performance under controlled compression, resolution degradation, audio noise, re-encoding, frame loss and audio/video temporal offsets.

### Gap 4 — Binary predictions are difficult to audit

A forensic user needs more than REAL/FAKE. We will investigate modality-level confidence, visual attribution, temporal evidence and cross-modal mismatch indicators.

### Gap 5 — Dataset shortcuts can produce misleading results

Recent work shows that audio-visual detectors may exploit accidental dataset properties. We will actively test for shortcut behavior and document dataset limitations rather than treating benchmark accuracy as proof of forensic validity.

### Gap 6 — Localization is underdeveloped in our initial scope

Our first objective is reliable clip-level detection. Segment/frame/region localization will be treated as an extension and will only be claimed if the data and experiments support it.

## Resulting research direction

The project will investigate a robust, explainable audio-visual detector that combines modality-specific evidence with cross-modal consistency and evaluates generalization under manipulation shift and realistic perturbations.

## What is *not* claimed as novelty

- Using audio and video together.
- Using CNNs, transformers, pretrained encoders, or Grad-CAM individually.
- Feature concatenation or simple score averaging.
- Testing compression individually.
- Binary real/fake classification.

The contribution must be established by the complete experimental design and demonstrated results.
