from __future__ import annotations

from collections.abc import Iterable

import pandas as pd


def require_columns(df: pd.DataFrame, columns: Iterable[str], name: str) -> None:
    missing = [column for column in columns if column not in df.columns]
    if missing:
        raise ValueError(f"{name} is missing required columns: {missing}")

