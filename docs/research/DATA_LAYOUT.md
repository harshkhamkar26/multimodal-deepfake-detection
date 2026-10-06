# Data Layout and Storage Policy

## Purpose

This document defines the local, Google Drive, Colab, and GitHub roles for the LAV-DF dataset used by the Multimodal Deepfake Detection System.

## Canonical local project layout

The Windows project root should contain the raw LAV-DF dataset under `data\\raw\\LAV-DF`:

```
multimodal-deepfake-detection-system/
├── data/
│   ├── raw/
│   │   └── LAV-DF/
│   │       ├── train/
│   │       ├── dev/
│   │       └── test/
│   ├── metadata/
│   ├── manifests/
│   ├── splits/
│   ├── cache/
│   ├── checkpoints/
│   └── logs/
├── features/
│   ├── audio/
│   └── visual/
├── experiments/
├── results/
├── configs/
├── docs/
├── notebooks/
├── src/
├── tests/
└── scripts/
```

The exact contents of `train`, `dev`, and `test` will be verified from the downloaded LAV-DF release before preprocessing.

## Current downloaded dataset

The current downloaded dataset is approximately 25 GB and contains paired audio-visual media. The verified local dataset root is now:

```
data\\raw\\LAV-DF
```

with the dataset-provided splits:

```
data\\raw\\LAV-DF\\train
data\\raw\\LAV-DF\\dev
data\\raw\\LAV-DF\\test
```

The obsolete `data\\archive (7)` wrapper was empty after the move and has been removed. The raw dataset must remain unchanged after placement; preprocessing outputs belong in separate directories.

## Google Colab / Google Drive layout

For Colab, the persistent copy should use:

```
My Drive/
└── multimodal-deepfake-detection/
    ├── data/
    │   ├── raw/
    │   │   └── LAV-DF/
    │   │       ├── train/
    │   │       ├── dev/
    │   │       └── test/
    │   ├── manifests/
    │   ├── splits/
    │   ├── checkpoints/
    │   └── logs/
    ├── features/
    │   ├── audio/
    │   └── visual/
    ├── experiments/
    ├── results/
    └── configs/
```

Raw media remains persistent on Drive. During expensive preprocessing, only the active chunk should be staged to Colab's local `/content` storage when beneficial.

## Manifest-first processing

The pipeline will create persistent manifests instead of repeatedly recursively scanning and decoding the full dataset.

Recommended manifest fields include:

- sample ID
- split
- media path(s)
- label
- source/identity information when available
- manipulation information when available
- duration
- frame/audio metadata
- validation status
- preprocessing status
- chunk ID
- error information

The manifest is metadata; it is not a copy of the raw dataset.

## Chunking and checkpointing

Large-scale preprocessing must be resumable.

Example:

```
chunk_0001 -> completed
chunk_0002 -> completed
chunk_0003 -> completed
...
chunk_0018 -> in progress
```

A persistent checkpoint records completed chunks. If the Colab runtime restarts, processing resumes from the first incomplete chunk rather than starting over.

## GitHub policy

Raw LAV-DF media, extracted audio/video, model checkpoints, and other large generated artifacts must **not** be committed to GitHub.

GitHub stores:

- source code
- notebooks
- configuration templates
- documentation
- manifests/schema definitions
- experiment metadata
- tests
- reproducibility instructions

Local/Drive storage stores:

- LAV-DF raw media
- generated features
- checkpoints
- large experiment outputs

## Research split policy

The `train`, `dev`, and `test` directories must be preserved as dataset-provided splits unless the verified metadata requires a research-specific leakage-safe split.

The project will not silently mix files between these splits.

## Important rule

Do not rename individual LAV-DF media files or modify the raw dataset contents until the dataset metadata, labels, pairing and split semantics have been inspected and recorded in the M1 manifest.
