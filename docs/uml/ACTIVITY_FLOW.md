# UML-03 — Activity Flow Specification

## End-to-End Inference Activity

```text
[Start]
   |
   v
Receive Video
   |
   v
Validate Input
   |
   +---- invalid ----> Return Validation Error --> [End]
   |
 valid
   v
Inspect Media
   |
   +---------------------------+
   |                           |
   v                           v
Extract/Sample Frames      Extract Audio
   |                           |
   v                           v
Visual Preprocessing       Audio Preprocessing
   |                           |
   v                           v
Visual Representation     Audio Representation
   |                           |
   v                           v
Temporal Aggregation      Audio Temporal Aggregation
   |                           |
   +-------------+-------------+
                 |
                 v
           Fusion Module
                 |
                 v
       Authenticity Scoring
                 |
        +--------+--------+
        |                 |
        v                 v
 Calibration Check   Evidence Generation
        |                 |
        +--------+--------+
                 |
                 v
         Construct Result
                 |
                 v
         Display / Return
                 |
                [End]
```

## Research Training Activity

```text
[Start]
   |
   v
Audit Dataset
   |
   v
Freeze Split Protocol
   |
   v
Configure Experiment
   |
   v
Prepare Training Data
   |
   +-------------------+-------------------+
   |                   |                   |
   v                   v                   v
Train Video        Train Audio        Train Simple
Baseline           Baseline           Fusion Baseline
   |                   |                   |
   +-------------------+-------------------+
                       |
                       v
                Compare Baselines
                       |
                       v
             Select Research Design
                       |
                       v
                Train Proposed Fusion
                       |
              +--------+--------+
              |                 |
              v                 v
          Ablation       Generalization
              |                 |
              +--------+--------+
                       |
                       v
                  Robustness
                       |
                       v
                  Error Analysis
                       |
                       v
               Freeze Results
                       |
                       v
              Paper / Demo Prep
                       |
                      [End]
```

## Decision Points

1. **Input valid?** If no, stop inference and return an input error.
2. **Audio available?** If the selected inference mode requires audio and it is unavailable, return a defined modality-unavailable state rather than silently fabricating an audio signal.
3. **Model artifact available?** If no compatible artifact exists, inference cannot proceed.
4. **Research gate passed?** Proposed-model evaluation begins only after baseline protocol is stable.
5. **Generalization protocol valid?** Evaluation is reported only when the training/test conditions are clearly defined and leakage risks are addressed.
