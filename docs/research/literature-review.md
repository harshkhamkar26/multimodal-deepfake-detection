# Literature Review

## Purpose

The literature review establishes what has already been demonstrated in deepfake detection and prevents us from presenting existing ideas as new contributions.

## Core papers and systems

| Work | Main contribution | Relevance to our project |
|---|---|---|
| FaceForensics++ (Rossler et al.) | Large benchmark for facial manipulation detection and standardized evaluation | Foundational visual deepfake detection baseline |
| Celeb-DF (Li et al.) | Higher-quality celebrity deepfake dataset designed to reduce obvious artifacts | Useful for realistic visual evaluation |
| DeepFake Detection Challenge (DFDC) | Large-scale benchmark focused on diverse deepfakes | Supports cross-dataset/generalization thinking |
| FakeAVCeleb (Khalid et al.) | Audio-visual deepfake dataset combining manipulated faces and synthetic/cloned audio | Directly relevant multimodal benchmark |
| DeepfakeBench (Yan et al.) | Unified benchmark framework covering datasets, preprocessing, detectors and evaluation | Reference for reproducible benchmarking |
| AV-Deepfake1M (Cai et al.) | Large-scale audio-visual dataset with multimodal manipulations and localization tasks | Important source for multimodal and localization research |
| Audio-Visual Deepfake Detection System Using Multimodal Deep Learning | Combines audio and visual evidence for deepfake classification | Establishes that basic multimodal fusion is not itself novel |
| Multi-modal Deepfake Detection via Multi-task Audio-Visual Prompt Learning | Uses multimodal representations, prompt learning and audio-visual consistency-oriented tasks | Relevant advanced multimodal direction |
| Circumventing Shortcuts in Audio-visual Deepfake Detection Datasets with Unsupervised Learning | Shows that detectors can exploit dataset shortcuts rather than genuine forgery evidence | Strong motivation for leakage, shortcut and robustness testing |
| AV-Deepfake1M++ | Extends audio-visual benchmark evaluation toward realistic perturbations | Supports robustness-under-distortion experiments |
| Investigating Self-Supervised Representations for Audio-Visual Deepfake Detection | Studies self-supervised audio-visual representations | Relevant future/advanced representation-learning direction |
| Inconsistency-aware Multimodal Schrodinger Bridge for Deepfake Localization | Uses multimodal inconsistency for localization | Motivates future segment/region localization capability |

## Literature themes

### 1. Unimodal detection

Video-only systems can identify spatial and temporal artifacts in manipulated faces. Audio-only systems can identify synthetic speech and acoustic artifacts. These are necessary baselines but each observes only part of the evidence.

### 2. Multimodal detection

Audio-visual systems combine evidence from separate modalities. The literature shows that multimodal information can be useful, but simple concatenation or averaging should not automatically be described as a research contribution.

### 3. Cross-modal consistency

A manipulated video may have plausible audio and plausible visuals independently while the relationship between them is inconsistent. Lip-to-speech alignment, timing and semantic/temporal correspondence therefore provide a distinct forensic signal.

### 4. Generalization

Performance on a random split from the same dataset can overestimate real-world effectiveness. Identity leakage, source-video leakage, manipulation-specific artifacts and dataset shortcuts can produce misleadingly high scores.

### 5. Robustness

Real deployments involve compression, re-encoding, resolution changes, background noise, missing frames and audio/video timing changes. Robustness should therefore be measured explicitly rather than assumed from clean benchmark accuracy.

### 6. Explainability

A useful forensic system should expose confidence and evidence instead of returning only a binary label. Visual attribution, modality-level confidence and cross-modal mismatch indicators are candidate explanations.

## Primary references

- FaceForensics++: https://arxiv.org/abs/1901.08971
- Celeb-DF: https://arxiv.org/abs/1909.12962
- DFDC: https://arxiv.org/abs/2006.07397
- FakeAVCeleb: https://arxiv.org/abs/2108.05080
- DeepfakeBench: https://arxiv.org/abs/2307.01426
- AV-Deepfake1M: https://arxiv.org/abs/2311.15308
- Multi-modal Deepfake Detection via Multi-task Audio-Visual Prompt Learning: https://ojs.aaai.org/index.php/AAAI/article/view/32042
- CVPR 2025 shortcut study: https://openaccess.thecvf.com/content/CVPR2025/html/Smeu_Circumventing_Shortcuts_in_Audio-visual_Deepfake_Detection_Datasets_with_Unsupervised_Learning_CVPR_2025_paper.html
- AV-Deepfake1M project: https://github.com/ControlNet/AV-Deepfake1M
- CVPR 2026 localization work: https://openaccess.thecvf.com/content/CVPR2026/html/Xiong_Inconsistency-aware_Multimodal_Schrodinger_Bridge_for_Deepfake_Localization_CVPR_2026_paper.html

## Review status

This is the initial research map. Before the final paper, every selected reference will be verified, categorized, and recorded with publication venue, year, dataset, architecture, metrics, limitations, and exact relevance to our experiments.
