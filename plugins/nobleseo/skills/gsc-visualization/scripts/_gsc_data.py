"""Shared input helpers for the chart scripts.

Reads a CSV file (for example a Google Search Console "Performance" export) or a
JSON file holding a list of records. Percentage strings such as "5.2%" become
numbers (5.2) so that CTR columns from GSC exports can be plotted directly.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Iterable

import pandas as pd

_PERCENT = re.compile(r"^\s*-?\d+(?:[.,]\d+)?\s*%\s*$")
_WEEKDAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]


def _percent_to_number(series: pd.Series) -> pd.Series:
    present = series.dropna()
    if present.empty or not present.map(lambda v: bool(_PERCENT.match(str(v)))).all():
        return series
    # Missing values stay missing; only present values are cleaned and converted.
    return series.map(
        lambda v: float(str(v).replace("%", "").replace(",", ".").strip()) if pd.notna(v) else float("nan")
    ).astype(float)


def load_table(path: str) -> pd.DataFrame:
    """Load ``path`` as a DataFrame; the format follows the file extension."""
    file = Path(path)
    suffix = file.suffix.lower()
    if suffix == ".csv":
        df = pd.read_csv(file)
    elif suffix == ".json":
        with file.open(encoding="utf-8") as handle:
            data = json.load(handle)
        if isinstance(data, dict) and isinstance(data.get("rows"), list):
            data = data["rows"]
        df = pd.DataFrame(data)
    else:
        raise ValueError(f"Unsupported data file type '{suffix}'. Use .csv or .json.")
    for column in df.columns:
        if pd.api.types.is_object_dtype(df[column]) or pd.api.types.is_string_dtype(df[column]):
            df[column] = _percent_to_number(df[column])
    return df


def require_columns(df: pd.DataFrame, columns: Iterable[str | None]) -> None:
    """Stop with an error listing every requested column that is not in the data."""
    missing = [c for c in columns if c and c not in df.columns]
    if missing:
        available = ", ".join(map(str, df.columns))
        print(f"Error: column(s) not found: {', '.join(missing)}. Available: {available}", file=sys.stderr)
        sys.exit(1)


def require_rows(df: pd.DataFrame, reason: str) -> None:
    """Stop when filtering left nothing to plot."""
    if df.empty:
        print(f"Error: no rows left to plot ({reason})", file=sys.stderr)
        sys.exit(1)


def weekday_order(labels: Iterable[object]) -> list[object] | None:
    """Return ``labels`` in Monday→Sunday order when every label is a weekday name or abbreviation."""
    labels = list(labels)
    positions = {}
    for label in labels:
        key = str(label).strip().lower()
        match = next((i for i, day in enumerate(_WEEKDAYS) if len(key) >= 2 and day.startswith(key)), None)
        if match is None:
            return None
        positions[label] = match
    return sorted(labels, key=positions.__getitem__)
