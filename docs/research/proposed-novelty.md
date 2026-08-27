# Proposed Novelty

> These are proposed contributions, not established claims. They become research claims only after implementation and controlled experiments support them.

## Proposed contribution 1 — Evidence-aware multimodal fusion

Build separate visual and audio branches, then combine their learned evidence rather than treating the entire input as one undifferentiated signal.

## Proposed contribution 2 — Cross-modal consistency signal

Measure whether visual speech activity and audio speech evidence agree over time. The model should be able to identify cases where both modalities appear plausible individually but conflict with one another.

Candidate signals include:

- mouth/lip motion versus speech timing
- audio/video temporal alignment
- modality confidence disagreement
- learned audio-visual embedding similarity or compatibility

## Proposed contribution 3 — Robustness-aware evaluation

Evaluate the same trained detector under controlled real-world perturbations:

- video compression and re-encoding
- reduced resolution
- frame dropping or temporal degradation
- background/environmental audio noise
- audio quality degradation
- controlled audio/video temporal offsets

Report both absolute performance and degradation from the clean condition.

## Proposed contribution 4 — Cross-manipulation generalization

Train on selected manipulation families and test on manipulation conditions withheld from training where dataset design permits it. The key question is whether the detector learns transferable forensic cues instead of memorizing manipulation-specific artifacts.

## Proposed contribution 5 — Explainable forensic output

Return a structured result containing:

- final REAL/FAKE prediction
- calibrated confidence where appropriate
- visual evidence/attribution
- audio evidence
- cross-modal consistency score
- dominant evidence contributing to the decision

The explanation must be presented as model evidence, not as an unsupported causal statement.

## Proposed contribution 6 — Systematic ablation framework

Quantify the value of each component by comparing:

1. visual-only
2. audio-only
3. simple fusion
4. proposed fusion without consistency
5. proposed fusion with consistency
6. proposed system with robustness-aware training, if implemented

## Proposed contribution 7 — Research-grade failure analysis

Do not report only aggregate metrics. Analyze false positives and false negatives by manipulation type, identity/source, modality conflict, video quality, audio quality and perturbation condition where metadata supports the analysis.

## Target contribution statement

The intended research contribution is a unified and reproducible framework for audio-visual deepfake detection that combines modality-specific forensic evidence with cross-modal consistency analysis and evaluates robustness, unseen-manipulation generalization, and interpretability under controlled experimental conditions.
