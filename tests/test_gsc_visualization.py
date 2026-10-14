import json
import os
import subprocess
import sys
from pathlib import Path

import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "plugins" / "nobleseo" / "skills" / "gsc-visualization" / "scripts"
FIXTURES = ROOT / "tests" / "fixtures"
sys.path.insert(0, str(SCRIPTS))

from _gsc_data import load_table, weekday_order  # noqa: E402


def run(script, *args, tmp_path):
    output = tmp_path / "chart.png"
    env = {**os.environ, "MPLBACKEND": "Agg"}
    command = [sys.executable, str(SCRIPTS / script), *args, "--title", "t", "--output", str(output)]
    return subprocess.run(command, capture_output=True, text=True, env=env), output


def test_percent_strings_become_numbers_with_json_nulls(tmp_path):
    path = tmp_path / "rows.json"
    path.write_text(json.dumps([{"CTR": "5.2%"}, {"CTR": None}, {"CTR": "1,5 %"}]), encoding="utf-8")
    ctr = load_table(str(path))["CTR"]
    assert ctr.iloc[0] == pytest.approx(5.2)
    assert pd.isna(ctr.iloc[1])
    assert ctr.iloc[2] == pytest.approx(1.5)


def test_percent_strings_become_numbers_with_csv_blanks(tmp_path):
    path = tmp_path / "rows.csv"
    path.write_text("Query,CTR\na,5.2%\nb,\nc,10%\n", encoding="utf-8")
    ctr = load_table(str(path))["CTR"]
    assert pd.api.types.is_float_dtype(ctr)
    assert pd.isna(ctr.iloc[1])
    assert ctr.iloc[2] == pytest.approx(10.0)


def test_mixed_text_column_is_left_alone(tmp_path):
    path = tmp_path / "rows.csv"
    path.write_text("Label\n5%\nother\n", encoding="utf-8")
    assert list(load_table(str(path))["Label"]) == ["5%", "other"]


def test_unsupported_extension_is_refused(tmp_path):
    path = tmp_path / "rows.xlsx"
    path.write_text("x", encoding="utf-8")
    with pytest.raises(ValueError):
        load_table(str(path))


@pytest.mark.parametrize("labels,expected", [
    (["Fri", "Mon", "Sun", "Tue"], ["Mon", "Tue", "Fri", "Sun"]),
    (["sunday", "Monday"], ["Monday", "sunday"]),
    (["Mon", "Holiday"], None),
    ([0, 3, 6], None),
])
def test_weekday_order(labels, expected):
    assert weekday_order(labels) == expected


@pytest.mark.parametrize("script,args", [
    ("gsc_timeseries.py", ["--data", str(FIXTURES / "gsc_daily.csv"), "--x", "Date", "--y", "Clicks", "Typo"]),
    ("gsc_timeseries.py", ["--data", str(FIXTURES / "gsc_daily.csv"), "--x", "Date", "--y", "Clicks", "--y2", "Typo"]),
    ("gsc_comparison.py", ["--data", str(FIXTURES / "gsc_daily.csv"), "--x", "Date", "--metrics", "Clicks", "Typo"]),
    ("gsc_bar.py", ["--data", str(FIXTURES / "gsc_queries.csv"), "--x", "Top queries", "--y", "Clicks", "--color-by", "Typo"]),
    ("gsc_scatter.py", ["--data", str(FIXTURES / "gsc_queries.csv"), "--x", "Position", "--y", "CTR", "--size", "Typo"]),
    ("gsc_pie.py", ["--data", str(FIXTURES / "gsc_devices.csv"), "--labels", "Device", "--values", "Typo"]),
    ("gsc_heatmap.py", ["--data", str(FIXTURES / "gsc_hourly.json"), "--x", "day_of_week", "--y", "hour", "--value", "Typo"]),
])
def test_missing_requested_column_stops_without_a_chart(tmp_path, script, args):
    result, output = run(script, *args, tmp_path=tmp_path)
    assert result.returncode == 1
    assert "Typo" in result.stderr
    assert not output.exists()


def test_scatter_with_constant_sizes_and_constant_x(tmp_path):
    path = tmp_path / "flat.csv"
    path.write_text("Position,CTR,Impressions\n3,1.0,100\n3,2.0,100\n3,3.0,100\n", encoding="utf-8")
    result, output = run("gsc_scatter.py", "--data", str(path), "--x", "Position", "--y", "CTR",
                         "--size", "Impressions", "--trendline", tmp_path=tmp_path)
    assert result.returncode == 0, result.stderr
    assert "trendline skipped" in result.stderr
    assert output.exists()


def test_timeseries_without_valid_dates_stops(tmp_path):
    path = tmp_path / "bad.csv"
    path.write_text("Date,Clicks\nnot-a-date,1\n", encoding="utf-8")
    result, output = run("gsc_timeseries.py", "--data", str(path), "--x", "Date", "--y", "Clicks", tmp_path=tmp_path)
    assert result.returncode == 1
    assert not output.exists()


def test_comparison_numeric_x_and_stacked_normalized(tmp_path):
    path = tmp_path / "hours.csv"
    path.write_text("hour,a,b\n0,1,4\n1,2,3\n2,3,2\n", encoding="utf-8")
    result, output = run("gsc_comparison.py", "--data", str(path), "--x", "hour", "--metrics", "a", "b",
                         "--normalize", "--stacked", tmp_path=tmp_path)
    assert result.returncode == 0, result.stderr
    assert output.exists()
