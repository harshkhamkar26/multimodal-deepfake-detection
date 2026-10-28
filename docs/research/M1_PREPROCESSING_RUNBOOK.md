# M1 Runbook — LAV-DF Metadata Audit

## Goal

Before decoding media, inspect the LAV-DF metadata schema, verify official split folders, derive provisional binary/four-class labels, and check whether metadata file paths resolve. This audit does not modify raw data or extract features.

## 1. Verify the local environment

Open Command Prompt in the local repository checkout. The repository checkout path may differ from the dataset path.

    git status --short
    python --version
    python -m pip show pandas matplotlib

The dataset root should contain metadata.json and the official train, dev, and test folders.

Expected dataset root for this Windows setup:

    C:\Users\Harsh\OneDrive - Universal Ai University\Desktop\multimodal-deepfake-detection-system\data\raw\LAV-DF

Do not add raw dataset files, extracted media, feature caches, or checkpoints to Git.

## 2. Install audit dependencies if missing

    python -m pip install pandas matplotlib

## 3. Run the audit

From the local repository root:

    python scripts\01_explore_lavdf.py --dataset-root "C:\Users\Harsh\OneDrive - Universal Ai University\Desktop\multimodal-deepfake-detection-system\data\raw\LAV-DF"

You can override the output directory with --output-dir "results\eda".

## 4. Expected outputs

The script writes these generated artifacts under results/eda/:

- metadata_inventory.csv: metadata records plus normalized labels, resolved paths, and audit fields.
- label_counts_by_split.csv: provisional binary label counts by split.
- duration_distribution.png: duration distribution, with units left as recorded in metadata.

The console prints record count, fields, split distribution, binary/four-class counts, unresolved paths, invalid labels, and duration summary.

## 5. Interpret the audit carefully

- label_binary = 0 means n_fakes == 0; label_binary = 1 means n_fakes > 0. Missing or non-numeric n_fakes remains unknown, not real.
- Four-class labels use modify_video and modify_audio: real, video-only fake, audio-only fake, both fake. Missing or unrecognized flags remain unknown.
- media_exists = False means none of the metadata-grounded candidate paths resolved. It does not prove a file is absent; the metadata path convention may need adjustment after inspecting a few records.
- Duration units are not assumed. Confirm the documented unit before converting timestamps or interpreting values as seconds.
- This is a metadata/path audit, not a full media decode check. Audio/video decoding checks belong in the next stage.
- Preserve the official train/dev/test assignments. Do not randomly repartition all videos.

## 6. What to send back for review

Share the printed output for record count and fields, split counts, binary/four-class counts, resolved/unresolved path totals, invalid label/duration counts, and any traceback. Do not upload the dataset or paste huge filename lists. A few sample metadata records with local paths redacted are enough if the schema needs inspection.
