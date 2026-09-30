# Dataset Selection Strategy

## Decision status

**Primary dataset: LAV-DF (Localized Audio-Visual DeepFake Dataset).**

LAV-DF is now the primary dataset for implementation and research experiments. The final experimental corpus remains conditional on successful local verification of access terms, files, labels, audio-video pairing, storage, and split integrity.

## Why LAV-DF

LAV-DF is an audio-visual deepfake dataset designed for localized manipulation analysis. It supports the project's central requirements: paired audio/video evidence, real/fake labels, temporal manipulation analysis, visual-only experiments, audio-only experiments and multimodal fusion.

The repository's earlier dataset candidates remain useful for literature comparison or future external validation, but they are not the current primary training corpus.

## Required verification before dataset freeze

1. Verify current access terms and academic-use conditions.
2. Obtain metadata/instructions and a small representative sample.
3. Decode both video and audio successfully.
4. Confirm labels and metadata.
5. Confirm audio-video temporal alignment.
6. Measure class and manipulation distributions.
7. Investigate identity/source overlap and duplicate risk.
8. Establish leakage-resistant train/validation/test splits.
9. Measure storage and preprocessing requirements.
10. Record the dataset version/access date used by the experiment.

## Acquisition strategy

### Phase A — Access verification
Obtain the official LAV-DF distribution and metadata without placing raw data in GitHub.

### Phase B — Pilot subset
Start with a small balanced pilot containing real and fake samples, multiple manipulation types where available, multiple identities/sources, and paired audio/video.

### Phase C — Restart-safe preprocessing
Generate a persistent manifest and process samples in chunks. Each completed item must record preprocessing status so Colab/runtime restarts do not force recomputation.

### Phase D — Dataset freeze
Freeze the experimental dataset only after decoding, pairing, labels, split integrity, storage and preprocessing have been verified.

## Research protocol enabled by LAV-DF

1. Visual-only baseline
2. Audio-only baseline
3. Simple multimodal fusion
4. Reliability-aware temporal fusion
5. Temporal localization where labels permit
6. Ablation studies
7. Cross-manipulation/generalization evaluation
8. Robustness evaluation
9. Modality-disagreement analysis
10. Error and calibration analysis

## Repository/data policy

Raw dataset videos/audio shall never be committed to GitHub.

The repository may contain:
- dataset documentation;
- official access instructions;
- metadata schemas;
- non-sensitive manifests;
- preprocessing code;
- split definitions;
- checksums where appropriate;
- experiment configurations;
- lightweight result summaries.

## Dataset decision rule

LAV-DF remains the primary dataset unless local verification shows that its access, integrity, licensing, storage, or metadata is unsuitable for the defined research protocol. Any replacement must be documented as a new dataset decision rather than silently changing the experiment corpus.
