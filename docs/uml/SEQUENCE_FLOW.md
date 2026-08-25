# UML-04 — Sequence Flow Specification

## Inference Sequence

```text
End User        UI/API        Inference        Video       Audio       Fusion       Explainer
   |               |              |               |           |           |             |
   |--upload------>|              |               |           |           |             |
   |               |--request--->|               |           |           |             |
   |               |              |--validate---->|           |           |             |
   |               |              |<--media info--|           |           |             |
   |               |              |-------------------------->|           |             |
   |               |              |<--------------------------|           |             |
   |               |              |--frames------>|           |           |             |
   |               |              |<--visual feat-|           |           |             |
   |               |              |--audio------------------->|           |             |
   |               |              |<--audio feat--------------|           |             |
   |               |              |------------------------------fusion-->|             |
   |               |              |<---------------------------score------|             |
   |               |              |----------------------------------------------->|
   |               |              |<----------------------------------evidence-------|
   |               |<--result-----|               |           |           |             |
   |<--display-----|              |               |           |           |             |
```

## Training/Evaluation Sequence

```text
Researcher -> Experiment Runner: select config
Experiment Runner -> Data Module: load approved split
Data Module -> Preprocessing: transform samples
Preprocessing -> Video Encoder: visual representation
Preprocessing -> Audio Encoder: audio representation
Video Encoder -> Fusion: visual features
Audio Encoder -> Fusion: audio features
Fusion -> Trainer: fused representation / score
Trainer -> Evaluator: predictions
Evaluator -> Metrics: calculate metrics
Metrics -> Researcher: results

Researcher -> Evaluator: request ablation/generalization
Evaluator -> Model: execute controlled condition
Model -> Evaluator: predictions
Evaluator -> Researcher: comparison + error analysis
```

## Sequence Principles

- Validation occurs before expensive model execution.
- Audio and video are independently observable for baseline and diagnostic purposes.
- Fusion consumes outputs from independently testable modality pipelines.
- Explanation is generated after prediction and must reference the model/version used for the prediction.
- Evaluation records the experiment configuration and split associated with each result.
