# Dataset Selection Strategy

## Decision status

**Primary dataset: NOT FINALIZED yet.**

The project requires a dataset that is genuinely accessible for the team, supports both audio and visual analysis, has real/fake labels, has acceptable research terms, and is practical to process.

## Candidates reviewed

| Dataset | Audio | Video | Access situation | Practical assessment |
|---|---|---|---|---|
| FakeAVCeleb | Yes | Yes | Request/approval required | Excellent research fit, but not immediate open access |
| DFDC | Yes in video files | Yes | Official access has prerequisites; full dataset is very large | Strong benchmark, but impractical as a full download for this project |
| FaceForensics++ | Not the primary modality | Yes | Access/request conditions | Strong visual benchmark, weak fit as the main multimodal dataset |
| AV-Deepfake1M/++ | Yes | Yes | Access/terms apply; very large | Excellent research benchmark, but too large for the first implementation |
| DigiFakeAV | Yes | Yes | Publicly released; repository/Hugging Face provide access | Strong current candidate, but full corpus is extremely large; use a verified subset if terms and storage permit |
| IAV-DF | Yes | Yes | Public sample is available | Promising Indian audio-video candidate; full-dataset availability must be verified before selection |

## Current selection criteria

A dataset can become the primary dataset only if all of the following are verified:

1. Free/open or otherwise acceptable academic access.
2. Both audio and visual information are available for the same samples.
3. Real and manipulated examples are present.
4. Labels and metadata are usable.
5. The download can realistically be completed with available storage/bandwidth.
6. The data supports visual-only, audio-only and multimodal experiments.
7. The license/terms are compatible with the project.
8. The provenance and dataset documentation are sufficiently clear.

## Important constraint

We will not commit raw datasets to GitHub. The repository will contain dataset documentation, download instructions, metadata schemas, preprocessing code, checksums where appropriate, and experiment records.

## Current research direction

The problem statement and system architecture remain unchanged. Dataset selection is an implementation constraint, not a change to the research question.

The planned experiments remain:

1. Visual-only baseline
2. Audio-only baseline
3. Simple multimodal fusion
4. Proposed multimodal fusion
5. Ablation studies
6. Robustness/generalization evaluation
7. Failure and modality-disagreement analysis

## Next action

Before downloading a large corpus, verify the exact current access method and obtain a small sample/subset. Inspect its labels, audio-video pairing, manipulation categories, class balance and file sizes. Only then freeze the primary dataset in the SRS and research plan.
