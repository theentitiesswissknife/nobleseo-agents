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


def render(monkeypatch, tmp_path, script, *args):
    """Run a chart script in-process and return the figure it saves."""
    import runpy

    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    captured = {}
    monkeypatch.setattr(plt, "savefig", lambda *a, **k: captured.setdefault("fig", plt.gcf()))
    monkeypatch.setattr(sys, "argv", [script, *args, "--title", "t", "--output", str(tmp_path / "chart.png")])
    runpy.run_path(str(SCRIPTS / script), run_name="__main__")
    return captured["fig"]


def test_bar_labels_sharing_a_prefix_keep_separate_bars(monkeypatch, tmp_path):
    path = tmp_path / "pages.csv"
    prefix = "https://www.example.org/blog/category/a-very-long-path/"
    path.write_text(f"Page,Clicks\n{prefix}one,30\n{prefix}two,20\n{prefix}three,10\n", encoding="utf-8")
    for orientation in ([], ["--horizontal"]):
        fig = render(monkeypatch, tmp_path, "gsc_bar.py", "--data", str(path), "--x", "Page", "--y", "Clicks", *orientation)
        ax = fig.axes[0]
        coords = [p.get_y() if orientation else p.get_x() for p in ax.patches]
        assert len(set(coords)) == 3


def test_comparison_keeps_numeric_x_and_fits_the_stack(monkeypatch, tmp_path):
    path = tmp_path / "hours.csv"
    path.write_text("hour,a,b\n0,1,4\n1,2,3\n2,3,2\n", encoding="utf-8")
    fig = render(monkeypatch, tmp_path, "gsc_comparison.py", "--data", str(path), "--x", "hour",
                 "--metrics", "a", "b", "--normalize", "--stacked")
    ax = fig.axes[0]
    assert ax.get_ylim()[1] >= 200
    assert ax.get_xlim()[1] < 10  # hours stay small numbers, not epoch dates


def test_smoothing_uses_calendar_days(monkeypatch, tmp_path):
    path = tmp_path / "gaps.csv"
    # 1 Jan and 20 Jan are 19 days apart: a 7-day window must not average them together
    path.write_text("Date,Clicks\n2026-01-01,10\n2026-01-20,100\n2026-01-21,200\n", encoding="utf-8")
    fig = render(monkeypatch, tmp_path, "gsc_timeseries.py", "--data", str(path), "--x", "Date", "--y", "Clicks", "--smooth")
    values = list(fig.axes[0].lines[0].get_ydata())
    assert values == [10, 100, 150]


def test_scatter_keeps_rows_without_a_category(monkeypatch, tmp_path):
    path = tmp_path / "rows.csv"
    path.write_text("Position,CTR,Device\n1,10,Mobile\n2,8,Desktop\n3,6,\n", encoding="utf-8")
    fig = render(monkeypatch, tmp_path, "gsc_scatter.py", "--data", str(path), "--x", "Position", "--y", "CTR", "--color", "Device")
    plotted = sum(len(collection.get_offsets()) for collection in fig.axes[0].collections)
    assert plotted == 3


def test_heatmap_mean_does_not_add_rates(monkeypatch, tmp_path):
    path = tmp_path / "ctr.csv"
    path.write_text("device,country,ctr\nMobile,IT,5%\nMobile,IT,10%\n", encoding="utf-8")
    result, _ = run("gsc_heatmap.py", "--data", str(path), "--x", "device", "--y", "country", "--value", "ctr",
                    "--agg", "mean", "--annotate", tmp_path=tmp_path)
    assert result.returncode == 0, result.stderr
    fig = render(monkeypatch, tmp_path, "gsc_heatmap.py", "--data", str(path), "--x", "device", "--y", "country",
                 "--value", "ctr", "--agg", "mean", "--annotate")
    assert [t.get_text() for t in fig.axes[0].texts] == ["7.5"]


def test_pie_with_zero_total_is_a_clear_error(tmp_path):
    path = tmp_path / "zero.csv"
    path.write_text("Device,Clicks\nMobile,0\nDesktop,0\n", encoding="utf-8")
    result, output = run("gsc_pie.py", "--data", str(path), "--labels", "Device", "--values", "Clicks", tmp_path=tmp_path)
    assert result.returncode == 1
    assert "total above zero" in result.stderr
    assert not output.exists()


def test_peak_annotation_skips_an_empty_metric(tmp_path):
    path = tmp_path / "empty.json"
    path.write_text(json.dumps([{"Date": f"2026-01-0{d}", "CTR": None, "Clicks": d} for d in (1, 2, 3)]), encoding="utf-8")
    result, output = run("gsc_timeseries.py", "--data", str(path), "--x", "Date", "--y", "Clicks", "CTR",
                         "--annotate-peaks", tmp_path=tmp_path)
    assert result.returncode == 0, result.stderr
    assert output.exists()


def test_pie_keeps_rows_without_a_label(monkeypatch, tmp_path):
    path = tmp_path / "devices.csv"
    path.write_text("Device,Clicks\nMobile,10\n,90\n", encoding="utf-8")
    fig = render(monkeypatch, tmp_path, "gsc_pie.py", "--data", str(path), "--labels", "Device", "--values", "Clicks")
    labels = sorted(t.get_text() for t in fig.axes[0].texts if t.get_text() in {"Mobile", "(missing)"})
    assert labels == ["(missing)", "Mobile"]


def test_heatmap_mean_leaves_absent_cells_empty(monkeypatch, tmp_path):
    path = tmp_path / "pos.csv"
    path.write_text("device,country,position\nMobile,US,5\nDesktop,GB,10\n", encoding="utf-8")
    fig = render(monkeypatch, tmp_path, "gsc_heatmap.py", "--data", str(path), "--x", "device", "--y", "country",
                 "--value", "position", "--agg", "mean", "--annotate")
    assert sorted(t.get_text() for t in fig.axes[0].texts) == ["10", "5"]


def test_heatmap_without_usable_cells_is_a_clear_error(tmp_path):
    path = tmp_path / "blank.csv"
    path.write_text("device,country,clicks\n,,5\n,,6\n", encoding="utf-8")
    result, output = run("gsc_heatmap.py", "--data", str(path), "--x", "device", "--y", "country", "--value", "clicks",
                         tmp_path=tmp_path)
    assert result.returncode == 1
    assert "no rows" in result.stderr
    assert not output.exists()
