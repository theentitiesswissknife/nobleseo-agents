"""Run every gsc-visualization script on the synthetic fixtures and check a PNG is produced."""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "plugins" / "nobleseo" / "skills" / "gsc-visualization" / "scripts"
FIXTURES = ROOT / "tests" / "fixtures"

CASES = {
    "timeseries": ["gsc_timeseries.py", "--data", "gsc_daily.csv", "--x", "Date", "--y", "Clicks", "Impressions",
                   "--y2", "Position", "--smooth", "--annotate-peaks"],
    "bar": ["gsc_bar.py", "--data", "gsc_queries.csv", "--x", "Top queries", "--y", "Clicks", "--horizontal",
            "--limit", "15", "--color-by", "CTR"],
    "pie": ["gsc_pie.py", "--data", "gsc_devices.csv", "--labels", "Device", "--values", "Clicks", "--donut",
            "--threshold", "3"],
    "scatter": ["gsc_scatter.py", "--data", "gsc_queries.csv", "--x", "Position", "--y", "CTR", "--size",
                "Impressions", "--trendline", "--invert-x"],
    "heatmap": ["gsc_heatmap.py", "--data", "gsc_hourly.json", "--x", "day_of_week", "--y", "hour", "--value",
                "clicks", "--annotate"],
    "comparison": ["gsc_comparison.py", "--data", "gsc_daily.csv", "--x", "Date", "--metrics", "Clicks",
                   "Impressions", "--normalize"],
}


def main() -> int:
    out_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(tempfile.mkdtemp())
    out_dir.mkdir(parents=True, exist_ok=True)
    failures = 0
    for name, (script, *args) in CASES.items():
        args = [str(FIXTURES / a) if a.endswith((".csv", ".json")) else a for a in args]
        output = out_dir / f"{name}.png"
        command = [sys.executable, str(SCRIPTS / script), *args, "--title", f"Smoke test: {name}", "--output", str(output)]
        result = subprocess.run(command, capture_output=True, text=True, env={"MPLBACKEND": "Agg", **__import__("os").environ})
        ok = result.returncode == 0 and output.exists() and output.read_bytes()[:8] == b"\x89PNG\r\n\x1a\n"
        print(f"{'ok  ' if ok else 'FAIL'} {name}")
        if not ok:
            failures += 1
            print(result.stdout, result.stderr, sep="\n")
    print(f"charts in {out_dir}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
