# Risk and Validity Protocol

## Purpose

This document defines the main threats to validity for the Multimodal Deepfake Detection System and the controls that must be applied before reporting research results.

The objective is not to maximize a single headline accuracy. The objective is to obtain the highest reliable performance under a defensible, reproducible evaluation protocol.

## 1. Data Leakage

**Risk:** Information from validation/test data, related samples, or preprocessing can influence training or model selection.

**Controls:**
- Freeze the final test protocol before final model selection.
- Fit training-dependent preprocessing only on training data.
- Keep test data out of hyperparameter tuning and threshold selection.
- Audit duplicate and near-duplicate relationships where feasible.

## 2. Identity and Source Leakage

**Risk:** The same identity, source material, or closely related recordings appear across splits, allowing the model to learn identity/source cues instead of manipulation evidence.

**Controls:**
- Inspect available identity/source metadata.
- Prefer identity/source-grouped splitting where the dataset supports it.
- Document any unavoidable overlap rather than silently ignoring it.

## 3. Manipulation Leakage

**Risk:** The detector learns generator- or manipulation-specific artifacts rather than general manipulation evidence.

**Controls:**
- Record manipulation categories explicitly.
- Where dataset structure permits, perform cross-condition/cross-manipulation evaluation.
- Compare in-distribution and shifted-condition performance.

## 4. Overfitting

**Risk:** The model memorizes training examples or dataset-specific patterns.

**Controls:**
- Use training/validation/test separation.
- Monitor validation loss and metrics.
- Use early stopping when appropriate.
- Use regularization, augmentation, weight decay, or freezing strategies where justified.
- Avoid repeated test-set inspection.

## 5. Hyperparameter Overfitting

**Risk:** Repeatedly changing architecture or hyperparameters based on validation results can effectively overfit the validation set.

**Controls:**
- Define a limited tuning protocol.
- Track experiments and decisions.
- Freeze the final configuration before final test evaluation.

## 6. Class Imbalance

**Risk:** A model can obtain high accuracy by favoring the majority class.

**Controls:**
- Report class distributions for every split.
- Consider class-weighted loss or balanced sampling where appropriate.
- Report F1, precision, recall, ROC-AUC, PR-AUC, and confusion matrix in addition to accuracy.

## 7. Shortcut Learning and Dataset Bias

**Risk:** The model learns compression, resolution, background, codec, recording environment, or other incidental cues correlated with labels.

**Controls:**
- Inspect quality and metadata distributions by class.
- Perform controlled robustness tests when feasible.
- Analyze failure cases and modality behavior.
- Avoid claiming that a high score proves the model learned a universal forensic signal.

## 8. Audio-Specific Risks

**Risks:**
- synthetic audio artifacts dominate the decision;
- audio quality differs systematically by class;
- audio is missing/corrupted;
- segmentation is inconsistent;
- audio-video synchronization is incorrect.

**Controls:**
- Define an explicit audio preprocessing pipeline.
- Validate audio/video temporal alignment.
- Record missing/corrupted modality cases.
- Maintain an audio-only baseline.
- Compare model behavior when audio is removed or degraded.

## 9. Video-Specific Risks

**Risks:**
- face detection/cropping errors;
- frame sampling bias;
- low-quality frames;
- model dependence on a particular face detector or preprocessing artifact.

**Controls:**
- Measure preprocessing failure rates.
- Version the face/frame preprocessing pipeline.
- Keep preprocessing identical between training and inference unless an experiment explicitly changes it.

## 10. Threshold Overfitting

**Risk:** Selecting a classification threshold using test data inflates reported classification metrics.

**Controls:**
- Select thresholds using training/validation procedures only.
- Keep the final test set isolated.
- Report the thresholding protocol.

## 11. Metric Selection Bias

**Risk:** Reporting only the metric that looks best can produce a misleading evaluation.

**Controls:**
- Predefine primary and secondary metrics.
- Report confusion matrices and class-wise metrics.
- Report ROC-AUC and PR-AUC where useful for imbalanced data.

## 12. Random-Seed Variability

**Risk:** A single run may be unusually good or bad.

**Controls:**
- Fix and record random seeds.
- For important experiments, use multiple seeds where compute permits.
- Report variability when it materially affects conclusions.

## 13. Missing-Modality Risk

**Risk:** Some inference samples may lack usable audio or visual information.

**Controls:**
- Define supported-input requirements.
- Define a missing-modality policy before final evaluation.
- Evaluate fallback behavior separately if implemented.

## 14. Generalization and External Validity

**Risk:** Strong in-dataset performance may not transfer to unseen manipulation methods, datasets, or real-world media.

**Controls:**
- Clearly define the training and evaluation distributions.
- Use cross-condition or cross-dataset testing when feasible.
- Treat external validation as evidence of transfer, not proof of universal generalization.
- State limitations explicitly in the paper.

## 15. Calibration and Confidence

**Risk:** A model's confidence score may not correspond to its actual probability of being correct.

**Controls:**
- Evaluate calibration when confidence is shown to users.
- Clearly distinguish model score/confidence from factual proof.
- Avoid presenting an uncalibrated score as a guaranteed probability.

## 16. Explainability Risk

**Risk:** Attribution maps can be overinterpreted as proof that a highlighted region is objectively manipulated.

**Controls:**
- Treat explanations as model-attribution evidence.
- Evaluate whether explanations are stable/useful where feasible.
- Avoid claims stronger than the explanation method supports.

## 17. Reproducibility

**Risk:** Results cannot be reproduced because data versions, configurations, seeds, dependencies, or checkpoints are unclear.

**Controls:**
- Track code in Git.
- Store experiment configurations.
- Record dataset/split versions and manifests.
- Record model/checkpoint identifiers.
- Pin important dependencies.
- Keep experiment logs and metric outputs.

## 18. Data Governance, Licensing, and Repository Safety

**Risk:** Raw media or restricted dataset material is accidentally committed to GitHub or redistributed improperly.

**Controls:**
- Do not commit raw dataset videos/audio to the repository.
- Keep dataset access/download instructions separate from data itself.
- Verify dataset access/license conditions before publication or redistribution.
- Maintain a `.gitignore` for datasets, checkpoints, caches, and generated media.

## 19. Compute and Engineering Risk

**Risk:** The chosen architecture is too expensive to train, making the project impossible to complete or reproduce.

**Controls:**
- Benchmark a small end-to-end pipeline first.
- Start with lightweight/pretrained baselines.
- Measure memory, training time, and inference time.
- Increase complexity only when the evidence justifies it.

## 20. Preprocessing/Inference Mismatch

**Risk:** Training uses one preprocessing pipeline while the demo uses another.

**Controls:**
- Implement shared, version-controlled preprocessing components.
- Store preprocessing configuration with model artifacts.
- Test inference using the same transformations used during evaluation.

## 21. Experimental Integrity Rules

1. The final test set is not used for model selection.
2. Test-derived observations do not trigger repeated retraining for the reported result.
3. Every baseline uses the same evaluation definitions as the proposed method.
4. Dataset filtering and split rules are documented before final evaluation.
5. Important experiments are tracked with configuration, seed, dataset/split version, and model version.
6. Failed experiments are retained in experiment logs rather than silently deleted from the research history.
7. Accuracy alone is never treated as sufficient evidence of robustness.
8. Claims in the paper must not exceed the evaluation actually performed.

## 22. Research Decision Gate

Before final results are reported, verify:

- [ ] Dataset structure audited
- [ ] Class distribution documented
- [ ] Identity/source relationships investigated
- [ ] Duplicate/near-duplicate risk investigated
- [ ] Manipulation categories documented
- [ ] Split protocol frozen
- [ ] Train/validation/test separation maintained
- [ ] Baselines completed
- [ ] Proposed fusion evaluated
- [ ] Ablation completed
- [ ] Generalization experiment completed where supported
- [ ] Robustness experiment completed where supported
- [ ] Error analysis completed
- [ ] Primary/secondary metrics predefined and reported
- [ ] Final test evaluation isolated
- [ ] Reproducibility artifacts recorded
- [ ] Dataset/license constraints checked
- [ ] Claims reviewed against actual evidence

## 23. Current Project Position

The project has completed its UML/system-design phase. The next research task is the dataset and literature audit. The exact model architecture, final split, and generalization protocol must remain provisional until the dataset is inspected and these risks are verified against the actual available metadata and data organization.
