# Research Roadmap

## Phase R0 — Scope and literature

- [x] Define multimodal audio-visual problem
- [x] Identify major benchmark families
- [x] Record research gaps
- [x] Define proposed contributions
- [ ] Complete paper-by-paper literature matrix

## Phase R1 — Dataset protocol

- [ ] Compare candidate datasets
- [ ] Confirm licenses and access
- [ ] Inspect metadata and manipulation labels
- [ ] Design identity/source leakage controls
- [ ] Freeze dataset versions and splits

## Phase R2 — Data pipeline

- [ ] Video sampling
- [ ] Face/region extraction
- [ ] Audio extraction
- [ ] Audio preprocessing
- [ ] Audio-video temporal alignment
- [ ] Dataset manifest generation
- [ ] Reproducibility checks

## Phase R3 — Baselines

- [ ] Train video-only baseline
- [ ] Train audio-only baseline
- [ ] Train simple multimodal baseline
- [ ] Establish metrics and compute budget

## Phase R4 — Proposed multimodal system

- [ ] Select visual representation
- [ ] Select audio representation
- [ ] Implement temporal modeling
- [ ] Implement fusion
- [ ] Implement cross-modal consistency signal
- [ ] Establish inference output schema

## Phase R5 — Research experiments

- [ ] Ablation studies
- [ ] Cross-manipulation evaluation
- [ ] Cross-dataset evaluation
- [ ] Unseen-manipulation evaluation where possible
- [ ] Robustness perturbation suite
- [ ] Cross-modal conflict experiments
- [ ] Efficiency analysis

## Phase R6 — Explainability and failure analysis

- [ ] Visual attribution
- [ ] Temporal evidence
- [ ] Modality confidence
- [ ] Cross-modal mismatch reporting
- [ ] False-positive analysis
- [ ] False-negative analysis
- [ ] Explanation stability checks

## Phase R7 — System and paper

- [ ] Inference application/demo
- [ ] Reproducibility package
- [ ] Final figures and tables
- [ ] Research limitations
- [ ] Final contribution claims
- [ ] Paper draft

## Current status

**R0 — Scope and literature foundation.**

The next research decision is dataset selection. Implementation should follow the frozen dataset and evaluation protocol, not precede it.
