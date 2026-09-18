# Dataset Selection Strategy

## Decision status

**Provisional primary dataset: LAV-DF (Localized Audio Visual DeepFake Dataset).**

The dataset is **not yet frozen as the final experimental corpus** until the team successfully obtains the files, verifies the current access terms, inspects a sample locally, and confirms that the available storage is sufficient.

## Why LAV-DF is currently the leading candidate

LAV-DF is specifically an **audio-visual deepfake dataset**, rather than a video-only dataset with audio merely present in the container. Public dataset documentation reports approximately **136,304 videos**, including **36,431 real and 99,873 fake videos**, with manipulations involving face reenactment, voice reenactment and transcript/content-driven forgery. The current Hugging Face distribution reports a total size of about **25.6 GB** and a **CC BY-NC 4.0** license, with terms that must be accepted before accessing the files.

For this project, that combination is important:

- paired audio + video
- real/fake data
- multimodal manipulation
- substantially smaller than DFDC/AV-Deepfake1M/DigiFakeAV
- publicly downloadable through documented mirrors
- suitable for visual-only, audio-only and multimodal experiments
- realistic for a controlled subset-first implementation

## Candidates reviewed

| Dataset | Audio | Video | Current access | Approx. size / scale | Project assessment |
|---|---|---|---|---|---|
| **LAV-DF** | Yes | Yes | Public download; terms must be accepted | ~25.6 GB; 136k videos reported | **Provisional primary candidate** |
| FakeAVCeleb | Yes | Yes | Request/approval required | 20,000 videos | Excellent research fit, but not immediate access |
| DFDC | Yes | Yes | Competition/AWS access conditions | ~124k videos; full training corpus is hundreds of GB | Too large and operationally heavy for first implementation |
| AV-Deepfake1M/++ | Yes | Yes | EULA/access conditions | >1M videos | Excellent benchmark, but too large for first implementation |
| DigiFakeAV | Yes | Yes | Public release; multiple distribution routes | 60,000 videos; multi-terabyte HF mirror | Strong modern candidate, but full corpus is too large |
| Global Multimedia Deepfake Detection (Multi-FFV) | Yes | Yes | Kaggle competition data / registration conditions | Large competition dataset | Strong multimodal benchmark, but persistent/reproducible access is less convenient |
| IAV-DF | Yes | Yes | Public sample is available | Full size not clearly documented in current README | Promising Indian candidate, but insufficient documentation to freeze it as primary |
| InDeepFake | Yes | Yes | Academic access request | Multimodal Indian dataset | Relevant, but restricted access |
| Deepfake-Eval-2024 | Yes | Yes | Public benchmark access | 44 h video + 56.5 h audio reported | Useful for **external evaluation**, not the main training corpus |

## Current selection criteria

A dataset can become the final primary dataset only if all of the following are verified:

1. Free or otherwise acceptable academic access.
2. Both audio and visual information are available for the same samples.
3. Real and manipulated examples are present.
4. Labels and metadata are usable.
5. Download size is realistic for the team's hardware and bandwidth.
6. The data supports visual-only, audio-only and multimodal experiments.
7. The license/terms are compatible with academic project use.
8. Provenance and dataset documentation are sufficiently clear.
9. Splits can be made without identity/source leakage.
10. A small local sample can be successfully decoded and paired before the full download.

## Recommended acquisition strategy

Do **not** immediately download the entire LAV-DF corpus.

### Phase A — access verification

1. Open the official LAV-DF repository/distribution.
2. Accept the dataset terms.
3. Download the metadata/instructions and a small representative sample if available.
4. Confirm that each sample provides usable video, audio and label information.

### Phase B — pilot subset

Start with a **small balanced pilot subset** rather than the full 25.6 GB corpus.

The pilot should contain:

- real samples
- fake samples
- multiple manipulation types where available
- multiple identities
- paired audio/video
- enough samples to test the complete preprocessing pipeline

The exact pilot size will be selected after inspecting the metadata and local storage.

### Phase C — dataset freeze

Freeze the dataset version only after:

- files decode correctly;
- audio and video are aligned;
- labels match the files;
- identity/source leakage can be controlled;
- class distribution is measured;
- storage and preprocessing time are measured.

Only then should the SRS and experiment configuration refer to the dataset as the **final primary dataset**.

## Research experiments remain unchanged

Dataset selection does not change the research question. The planned experiments remain:

1. Visual-only baseline
2. Audio-only baseline
3. Simple multimodal fusion
4. Proposed multimodal fusion
5. Ablation studies
6. Cross-manipulation/generalization evaluation
7. Robustness and failure analysis
8. Modality-disagreement analysis

## Important constraint

Raw datasets will **never** be committed to GitHub.

The repository will contain:

- dataset documentation
- official access/download instructions
- metadata schemas
- preprocessing code
- checksums where appropriate
- dataset version identifiers
- experiment configurations
- lightweight result summaries

## Dataset decision rule

If LAV-DF cannot be downloaded or used under acceptable academic terms, the next candidates to investigate are **DigiFakeAV (verified subset)** and **Global Multimedia Deepfake Detection / Multi-FFV**, subject to their current access conditions.

