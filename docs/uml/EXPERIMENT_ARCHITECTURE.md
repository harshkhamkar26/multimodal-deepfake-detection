# UML-09 — Research Experiment Architecture

## Experimental Structure

```text
                         Research Question
                               │
                               ▼
                        Dataset Audit
                               │
                               ▼
                       Freeze Split Protocol
                               │
          ┌────────────────────┼────────────────────┐
          ▼                    ▼                    ▼
     Video-only           Audio-only          Simple Fusion
      Baseline              Baseline             Baseline
          │                    │                    │
          └────────────────────┼────────────────────┘
                               ▼
                       Baseline Comparison
                               │
                               ▼
                      Proposed Multimodal
                            Fusion Model
                               │
                 ┌─────────────┼─────────────┐
                 ▼             ▼             ▼
              Ablation    Generalization  Robustness
                 │             │             │
                 └─────────────┼─────────────┘
                               ▼
                         Error Analysis
                               │
                               ▼
                    Final Research Conclusion
```

## Experiment Matrix

| Experiment | Question | Required comparison |
|---|---|---|
| E0 Data audit | Is the dataset/split valid? | leakage, duplicates, balance, identity/source relationships |
| E1 Video | How strong is visual evidence alone? | video-only metrics |
| E2 Audio | How strong is audio evidence alone? | audio-only metrics |
| E3 Simple fusion | Does basic multimodality help? | simple fusion vs unimodal |
| E4 Proposed fusion | Does the proposed design add value? | proposed vs E1/E2/E3 |
| E5 Ablation | Which components matter? | full model vs controlled removals |
| E6 Generalization | Does performance survive a defined distribution shift? | in-distribution vs cross-condition |
| E7 Robustness | How sensitive is the detector to media changes? | controlled perturbations |
| E8 Error analysis | Why does the model fail? | FP/FN/modality disagreement/calibration |

## Metrics

Primary metrics:

- ROC-AUC
- F1-score
- Precision
- Recall
- Accuracy

Additional metrics where applicable:

- PR-AUC
- calibration error
- confusion matrix
- condition-specific metrics
- inference/resource measurements

## Evaluation Rules

1. Freeze the test protocol before final model selection.
2. Use the same test set and metric definitions for competing models.
3. Do not tune hyperparameters on the test set.
4. Report class distribution and relevant split constraints.
5. Report both successes and important failures.
6. Avoid unsupported claims of universal generalization or state-of-the-art performance.
7. Record experiment configuration and model/preprocessing versions.

## High-Accuracy Strategy

The project may optimize performance through:

- appropriate preprocessing;
- class-imbalance handling;
- validated pretrained representations;
- controlled fine-tuning;
- hyperparameter tuning on validation data;
- appropriate temporal sampling;
- fusion optimization;
- calibration and threshold selection.

However, headline accuracy must never replace leakage-resistant evaluation and generalization analysis.

## Publication Readiness Gate

A research result is considered ready for paper inclusion only when:

- the dataset/split protocol is documented;
- baselines are reproducible;
- the proposed method is clearly defined;
- ablations are complete;
- generalization/robustness experiments are complete where supported;
- metrics and failure analysis are available; and
- the reported result can be reproduced from repository configuration and documented artifacts.
