"""Shared input loader for the chart scripts.

Reads a CSV file (for example a Google Search Console "Performance" export) or a
JSON file holding a list of records. Percentage strings such as "5.2%" become
numbers (5.2) so that CTR columns from GSC exports can be plotted directly.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

import pandas as pd

_PERCENT = re.compile(r"^\s*-?\d+(?:[.,]\d+)?\s*%\s*$")


def _percent_to_number(series: pd.Series) -> pd.Series:
    values = series.dropna().astype(str)
    if values.empty or not values.map(lambda v: bool(_PERCENT.match(v))).all():
        return series
    return series.astype(str).str.replace("%", "", regex=False).str.replace(",", ".", regex=False).str.strip().astype(float)


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
