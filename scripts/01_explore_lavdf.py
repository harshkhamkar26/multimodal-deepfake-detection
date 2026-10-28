"""
Step 1A — Inspect the local LAV-DF metadata and build an audit inventory.

Run from the repository root:
    python scripts/01_explore_lavdf.py --dataset-root "C:\\path\\to\\LAV-DF"

This script reads metadata and checks candidate media paths. It does not decode
videos, extract features, move/delete files, or modify the raw dataset.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

import matplotlib
matplotlib.use("Agg")  # Safe for headless runs and remote environments.
import matplotlib.pyplot as plt
import pandas as pd


EXPECTED_SPLITS = ("train", "dev", "test")
RECORD_KEYS = ("data", "metadata", "videos", "annotations", "records")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dataset-root",
        required=True,
        help="Directory containing metadata.json and the official train/dev/test folders.",
    )
    parser.add_argument(
        "--metadata",
        default="metadata.json",
        help="Metadata filename or path relative to --dataset-root (default: metadata.json).",
    )
    parser.add_argument(
        "--output-dir",
        default="results/eda",
        help="Output directory, relative to the current working directory unless absolute.",
    )
    parser.add_argument(
        "--preview-rows",
        type=int,
        default=5,
        help="Number of metadata records to print (default: 5).",
    )
    return parser.parse_args()


def load_records(json_path: Path) -> list[dict[str, Any]]:
    """Load common JSON layouts without silently guessing unsupported formats."""
    with json_path.open("r", encoding="utf-8-sig") as handle:
        payload = json.load(handle)

    if isinstance(payload, list):
        records = payload
    elif isinstance(payload, dict):
        records = None
        for key in RECORD_KEYS:
            if isinstance(payload.get(key), list):
                records = payload[key]
                print(f"Record list found under top-level key: {key}")
                break

        if records is None:
            if any(key in payload for key in ("file", "split", "n_fakes")):
                records = [payload]
            elif payload and all(isinstance(value, dict) for value in payload.values()):
                records = [
                    {"_metadata_key": key, **value}
                    for key, value in payload.items()
                ]
                print("Interpreting top-level dictionary as a mapping of records.")
            else:
                raise ValueError(
                    "Unsupported metadata structure. Top-level keys: "
                    f"{list(payload)[:40]}"
                )
    else:
        raise ValueError(
            f"Expected JSON object or array, got {type(payload).__name__}."
        )

    if not all(isinstance(record, dict) for record in records):
        raise ValueError("At least one metadata record is not a JSON object.")
    return records


def clean_split(value: Any) -> str | None:
    """Normalize split spelling while preserving unknown values for auditing."""
    if value is None or pd.isna(value):
        return None
    return str(value).strip().lower()


def as_bool(value: Any) -> bool | None:
    """Parse booleans conservatively; unknown values remain unknown."""
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)) and value in (0, 1):
        return bool(value)
    if isinstance(value, str):
        normalized = value.strip().lower()
        if normalized in {"true", "1", "yes", "y"}:
            return True
        if normalized in {"false", "0", "no", "n"}:
            return False
    return None


def four_class_label(row: pd.Series) -> str | None:
    """Map video/audio manipulation flags to the four requested classes."""
    video = as_bool(row.get("modify_video"))
    audio = as_bool(row.get("modify_audio"))
    if video is None or audio is None:
        return None
    if not video and not audio:
        return "real"
    if video and not audio:
        return "video_only_fake"
    if not video and audio:
        return "audio_only_fake"
    return "both_fake"


def candidate_media_paths(
    dataset_root: Path, split: str | None, file_value: Any
) -> list[Path]:
    """Try a few metadata-grounded locations; never recursively scan the dataset."""
    if file_value is None or pd.isna(file_value):
        return []

    raw = str(file_value).strip()
    if not raw:
        return []

    # Metadata may use Windows separators even when running on Linux/Colab.
    normalized = raw.replace("\\", "/")
    relative = Path(normalized)
    candidates: list[Path] = []

    if relative.is_absolute():
        candidates.append(relative)

    # Candidate 1: path as stored, relative to dataset root.
    candidates.append(dataset_root / relative)

    # Candidate 2: metadata may include the split prefix already.
    if split and relative.parts and relative.parts[0].lower() == split.lower():
        candidates.append(dataset_root / Path(*relative.parts[1:]))

    # Candidate 3: the file field may contain only a basename or a nested
    # path that lives under its official split folder.
    if split:
        candidates.append(dataset_root / split / relative.name)
        candidates.append(dataset_root / split / relative)

    # Deduplicate candidates without scanning the full dataset.
    unique: list[Path] = []
    seen: set[str] = set()
    for path in candidates:
        key = str(path).casefold()
        if key not in seen:
            unique.append(path)
            seen.add(key)
    return unique


def resolve_media_path(
    dataset_root: Path, split: str | None, file_value: Any
) -> str | None:
    for candidate in candidate_media_paths(dataset_root, split, file_value):
        if candidate.is_file():
            return str(candidate.resolve())
    return None


def safe_numeric(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series, errors="coerce")


def main() -> None:
    args = parse_args()
    dataset_root = Path(args.dataset_root).expanduser().resolve()
    metadata_path = Path(args.metadata)
    if not metadata_path.is_absolute():
        metadata_path = dataset_root / metadata_path
    output_dir = Path(args.output_dir).expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 72)
    print("LAV-DF METADATA AND PATH AUDIT")
    print("=" * 72)
    print(f"Dataset root: {dataset_root}")
    print(f"Dataset root exists: {dataset_root.is_dir()}")
    print(f"Metadata path: {metadata_path}")
    print(f"Metadata exists: {metadata_path.is_file()}")

    if not dataset_root.is_dir():
        raise FileNotFoundError(f"Dataset root does not exist: {dataset_root}")
    if not metadata_path.is_file():
        raise FileNotFoundError(f"metadata.json was not found: {metadata_path}")

    for split in EXPECTED_SPLITS:
        split_dir = dataset_root / split
        print(f"{split} directory exists: {split_dir.is_dir()}")

    records = load_records(metadata_path)
    df = pd.json_normalize(records, sep=".")
    print(f"\nMetadata records: {len(df):,}")
    print(f"Columns ({len(df.columns)}): {list(df.columns)}")

    # Keep the original columns, but use explicit normalized labels in the
    # generated audit inventory so downstream scripts have stable names.
    if "split" in df.columns:
        df["split_normalized"] = df["split"].map(clean_split)
    else:
        df["split_normalized"] = None

    if "n_fakes" in df.columns:
        n_fakes = safe_numeric(df["n_fakes"])
        df["n_fakes_numeric"] = n_fakes
        df["label_binary"] = pd.Series(pd.NA, index=df.index, dtype="Int64")
        valid_n_fakes = n_fakes.notna()
        df.loc[valid_n_fakes, "label_binary"] = (
            n_fakes.loc[valid_n_fakes] > 0
        ).astype(int)
    else:
        df["n_fakes_numeric"] = float("nan")
        df["label_binary"] = pd.Series(pd.NA, index=df.index, dtype="Int64")

    if "modify_video" in df.columns and "modify_audio" in df.columns:
        df["label_4class"] = df.apply(four_class_label, axis=1)
    else:
        df["label_4class"] = None

    if "duration" in df.columns:
        df["duration_numeric"] = safe_numeric(df["duration"])
    else:
        df["duration_numeric"] = float("nan")

    if "file" in df.columns:
        df["resolved_media_path"] = [
            resolve_media_path(dataset_root, split, file_value)
            for split, file_value in zip(
                df["split_normalized"], df["file"], strict=False
            )
        ]
        df["media_exists"] = df["resolved_media_path"].notna()
    else:
        df["resolved_media_path"] = None
        df["media_exists"] = False

    print("\n--- Split counts (metadata values) ---")
    print(df["split_normalized"].value_counts(dropna=False).to_string())

    print("\n--- Binary label counts (0=real, 1=fake) ---")
    print(
        df["label_binary"]
        .map({0: "real (0)", 1: "fake (1)"})
        .fillna("unknown / invalid")
        .value_counts(dropna=False)
        .to_string()
    )

    print("\n--- Four-class label counts ---")
    print(
        df["label_4class"]
        .fillna("unknown / invalid flags")
        .value_counts(dropna=False)
        .to_string()
    )

    print("\n--- Metadata / path checks ---")
    print("Missing file field:", int(df["file"].isna().sum()) if "file" in df else "field missing")
    print("Media paths resolved:", int(df["media_exists"].sum()))
    print("Media paths unresolved:", int((~df["media_exists"]).sum()))
    print("Invalid/missing binary labels:", int(df["label_binary"].isna().sum()))
    print("Invalid/missing durations:", int(df["duration_numeric"].isna().sum()))

    if "duration_numeric" in df:
        print("\n--- Duration statistics (metadata units not assumed) ---")
        print(df["duration_numeric"].describe().to_string())

        durations = df["duration_numeric"].dropna()
        if not durations.empty:
            fig, ax = plt.subplots(figsize=(8, 5))
            ax.hist(durations, bins=40)
            ax.set_title("LAV-DF duration distribution")
            ax.set_xlabel("Duration value (unit as stored in metadata)")
            ax.set_ylabel("Number of records")
            fig.tight_layout()
            fig.savefig(output_dir / "duration_distribution.png", dpi=150)
            plt.close(fig)

    if "split_normalized" in df and "label_binary" in df:
        crosstab = pd.crosstab(
            df["split_normalized"],
            df["label_binary"].map({0: "real", 1: "fake"}).fillna("unknown"),
            dropna=False,
        )
        print("\n--- Binary labels by split ---")
        print(crosstab.to_string())
        crosstab.to_csv(output_dir / "label_counts_by_split.csv")

    inventory_path = output_dir / "metadata_inventory.csv"
    df.to_csv(inventory_path, index=False)

    preview_columns = [
        column for column in
        ["file", "split", "n_fakes", "modify_video", "modify_audio",
         "duration", "label_binary", "label_4class", "media_exists"]
        if column in df.columns
    ]
    print(f"\n--- First {args.preview_rows} records ---")
    print(df[preview_columns].head(args.preview_rows).to_string(index=False))
    print(f"\nSaved full audit inventory: {inventory_path}")
    print(f"EDA outputs directory: {output_dir}")
    print("\nAudit complete. No raw media was changed or decoded.")


if __name__ == "__main__":
    main()
