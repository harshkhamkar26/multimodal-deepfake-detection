# Research Questions and Hypotheses

## Primary research question

Can an evidence-aware multimodal audio-visual deepfake detector improve robustness and cross-manipulation generalization over strong unimodal and simple-fusion baselines while providing interpretable evidence?

## Research questions

### RQ1 — Modality contribution

How much does audio improve detection beyond a strong visual-only baseline, and how much does visual evidence improve detection beyond a strong audio-only baseline?

### RQ2 — Fusion strategy

Does learned multimodal fusion outperform simple feature concatenation or score averaging?

### RQ3 — Cross-modal consistency

Does an explicit audio-visual consistency signal improve detection of multimodal or cross-modal manipulations?

### RQ4 — Generalization

How well does the proposed detector perform when the manipulation family, dataset, or source distribution differs from training?

### RQ5 — Robustness

How does performance degrade under compression, resolution changes, audio noise, re-encoding, frame degradation and controlled audio/video offsets?

### RQ6 — Explainability

Can the system provide evidence that is consistent with the modality responsible for the prediction and useful for human inspection?

### RQ7 — Efficiency

What accuracy/robustness improvement is obtained relative to computational cost, latency and model size?

## Hypotheses

- **H1:** Multimodal fusion will outperform the strongest unimodal baseline on appropriately controlled evaluation.
- **H2:** Explicit cross-modal consistency will improve detection for manipulations that create audio-visual disagreement.
- **H3:** Cross-manipulation performance will be lower than in-distribution performance, but the proposed model will degrade less than relevant baselines.
- **H4:** Realistic perturbations will reduce performance; robustness-aware methods, if implemented, will reduce the magnitude of degradation.
- **H5:** Explanation signals will correlate with the modality and temporal/visual regions that contribute most strongly to the model decision.

## Falsification criteria

The project will treat negative results as valid research findings. In particular, we will not force the novelty claim if:

- multimodal fusion does not beat strong unimodal baselines;
- consistency features add no measurable value;
- generalization does not improve;
- robustness gains disappear under proper cross-dataset testing; or
- explanations are unstable or misleading.
