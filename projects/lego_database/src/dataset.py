from __future__ import annotations

import argparse
from pathlib import Path

import kagglehub
import pandas as pd
from kagglehub import KaggleDatasetAdapter

from kaggle_lab.common.io import ensure_dir, write_dataframe
from kaggle_lab.common.validation import require_columns
from projects.lego_database.src.features import build_set_level_dataset

PROJECT_DIR = Path(__file__).resolve().parents[1]
RAW_DIR = PROJECT_DIR / "data" / "raw"
PROCESSED_DIR = PROJECT_DIR / "data" / "processed"
DATASET_SLUG = "rtatman/lego-database"
DATASET_FILES = [
    "sets.csv",
    "themes.csv",
    "inventories.csv",
    "inventory_parts.csv",
    "inventory_sets.csv",
    "parts.csv",
    "part_categories.csv",
    "colors.csv",
]


def download_tables(dataset_slug: str = DATASET_SLUG) -> dict[str, pd.DataFrame]:
    ensure_dir(RAW_DIR)
    tables: dict[str, pd.DataFrame] = {}

    for file_name in DATASET_FILES:
        df = kagglehub.load_dataset(
            KaggleDatasetAdapter.PANDAS,
            dataset_slug,
            file_name,
        )
        write_dataframe(df, RAW_DIR / file_name)
        tables[file_name] = df

    return tables


def load_raw_tables() -> dict[str, pd.DataFrame]:
    tables = {}
    for file_name in DATASET_FILES:
        path = RAW_DIR / file_name
        if not path.exists():
            raise FileNotFoundError(
                f"Missing raw file: {path}. Run `python -m projects.lego_database.src.dataset download`."
            )
        tables[file_name] = pd.read_csv(path)
    return tables


def validate_raw_tables(tables: dict[str, pd.DataFrame]) -> None:
    require_columns(tables["sets.csv"], ["set_num", "name", "year", "theme_id", "num_parts"], "sets")
    require_columns(tables["themes.csv"], ["id", "name"], "themes")
    require_columns(tables["inventories.csv"], ["id", "set_num"], "inventories")
    require_columns(tables["inventory_parts.csv"], ["inventory_id", "part_num", "color_id", "quantity"], "inventory_parts")


def build_processed_dataset() -> Path:
    tables = load_raw_tables()
    validate_raw_tables(tables)
    dataset = build_set_level_dataset(tables)
    return write_dataframe(dataset, PROCESSED_DIR / "set_level_features.csv")


def main() -> None:
    parser = argparse.ArgumentParser(description="Manage lego_database datasets.")
    parser.add_argument("command", choices=["download", "build"])
    args = parser.parse_args()

    if args.command == "download":
        download_tables()
        print(f"Downloaded raw tables to {RAW_DIR}")
        return

    output_path = build_processed_dataset()
    print(f"Built processed dataset at {output_path}")


if __name__ == "__main__":
    main()
