---
name: gsc-visualization
description: Create clear charts from Google Search Console or GA4 data — trends over time, top queries or pages, device and country shares, position vs CTR, day-by-hour patterns and multi-metric comparisons. Use when the user asks for a chart, graph, plot or visual summary of search or analytics data they have exported or retrieved.
---

# GSC and GA4 charts

Six ready-made chart scripts turn a Google Search Console (GSC) or GA4 table into a PNG chart. Use them instead of writing plotting code from scratch.

## Requirements

Python 3.10+ with `pandas`, `matplotlib`, `numpy`, `seaborn` and `scipy`. Check once with:

```bash
python -c "import pandas, matplotlib, numpy, seaborn, scipy"
```

If that fails, ask the user before installing anything (`python -m pip install pandas matplotlib numpy seaborn scipy`).

## Workflow

When discovered, NobleSEO `analytics_report_segments` supplies bounded persisted segment and daily heatmap cells. Retrieve every required page and preserve the exact project section, source grain, definitions and snapshot before charting. Ranking counts are source rows, not unique queries; preserve the native residual bucket caveat. Heatmap `imputed_zero` cells differ from observed zeros, and null/unobserved dates remain gaps. Do not combine a group calendar's fills with a performance calendar's missingness rule. Stored article `rank_history` requires separate content-read consent and retains engine/device/location/time; it is not GSC traffic or a new SERP check. Chart the retrieved observations without starting tracking, synchronization, provider work or materialization.

1. **Get the data.** Use a file the user provides: a GSC "Performance" export (CSV), a GA4 export (CSV), or a JSON list of rows. If the data comes from another tool the user has connected, save the rows to a `.json` file (a list of objects) or a `.csv` file in the working directory first.
2. **Check the columns.** Read the header and pick the exact column names for `--x`, `--y` and so on. GSC exports use names such as `Date`, `Top queries`, `Top pages`, `Clicks`, `Impressions`, `CTR`, `Position`. Percent values like `5.2%` are converted to numbers automatically.
3. **Run a script** from the `scripts/` folder next to this file, writing the chart into the working directory:

   ```bash
   python <this-skill-folder>/scripts/gsc_timeseries.py --data data.csv --x Date --y Clicks --title "Daily clicks" --output charts/daily-clicks.png
   ```

4. **Tell the user** where the chart was saved, and summarise what it shows in one or two sentences.

Create the `charts/` folder first if it does not exist. Never overwrite a user's file without asking.

## Choosing a chart

| Question | Script |
|---|---|
| How did a metric change over time? | `gsc_timeseries.py` |
| Which queries or pages lead? | `gsc_bar.py` |
| How is traffic split (device, country)? | `gsc_pie.py` |
| Is position related to CTR? | `gsc_scatter.py` |
| When do clicks happen (day × hour), or device × country? Weekday names or abbreviations are ordered Monday → Sunday. | `gsc_heatmap.py` |
| How do several metrics move together? | `gsc_comparison.py` |

All scripts take `--data` (CSV or JSON), `--title` and `--output`.

### `gsc_timeseries.py` — trends over time

`--x` date column; `--y` one or more metrics; optional:
- `--y2` metrics on a secondary axis (for `Position`, lower is better);
- `--smooth` (7-day rolling average over calendar days, so gaps in the dates are handled);
- `--annotate-peaks`;
- `--date-format` (default `%Y-%m-%d`).

```bash
python scripts/gsc_timeseries.py --data data.csv --x Date --y Clicks Impressions --y2 Position --smooth --title "Clicks, impressions and position" --output charts/trend.png
```

### `gsc_bar.py` — rankings

`--x` category column; `--y` value column; optional:
- `--limit` (default 10);
- `--horizontal` (better for long labels);
- `--sort asc|desc`;
- `--color-by` (colour bars by another metric).

```bash
python scripts/gsc_bar.py --data queries.csv --x "Top queries" --y Clicks --horizontal --limit 15 --color-by CTR --title "Top 15 queries by clicks" --output charts/top-queries.png
```

### `gsc_pie.py` — shares

`--labels` and `--values`; optional:
- `--donut`;
- `--explode N` (0-based slice index);
- `--threshold P` (group slices under P % as "Other").

Values must be non-negative with a total above zero. Rows without a label are shown as a "(missing)" slice.

```bash
python scripts/gsc_pie.py --data devices.csv --labels Device --values Clicks --donut --threshold 3 --title "Clicks by device" --output charts/devices.png
```

### `gsc_scatter.py` — correlation

`--x` and `--y`; optional:
- `--size` (bubble size column);
- `--color` (category column; rows without a category are shown as "(missing)");
- `--trendline`;
- `--invert-x` / `--invert-y` (use `--invert-x` when `Position` is on the X axis so that position 1 is on the right).

```bash
python scripts/gsc_scatter.py --data queries.csv --x Position --y CTR --size Impressions --trendline --invert-x --title "Position vs CTR" --output charts/position-ctr.png
```

### `gsc_heatmap.py` — two-dimensional patterns

`--x` (columns), `--y` (rows) and `--value`; optional:
- `--cmap` (default `YlOrRd`);
- `--annotate` (print values in cells);
- `--agg sum|mean` (default `sum`) for rows that share a cell. Use `sum` for clicks and impressions. `mean` is a plain, unweighted average of rows; cells with no rows stay empty.

  CTR and position must never be summed, and a plain average of them is usually wrong too. Before charting them, aggregate the data per cell: CTR = total clicks ÷ total impressions × 100, and position = impressions-weighted average of position. Save that table and chart it.

```bash
python scripts/gsc_heatmap.py --data hourly.json --x day_of_week --y hour --value clicks --annotate --title "Clicks by day and hour" --output charts/heatmap.png
```

### `gsc_comparison.py` — several metrics together

`--x` (usually a date) and `--metrics` (two or more); optional:
- `--normalize` (scale each metric to 0–100 %, so different units can share one axis);
- `--stacked` (stacked areas; with `--normalize` each layer is 0–100 % and the axis grows to fit the total).

```bash
python scripts/gsc_comparison.py --data daily.csv --x Date --metrics Clicks Impressions --normalize --title "Clicks vs impressions (normalised)" --output charts/comparison.png
```

## Style

Charts are saved at 150 DPI (time series, bar and comparison 12 × 6 inches; pie and scatter 10 × 8; heatmap 12 × 8) with a white background, light grid and a consistent colour palette, ready for reports and slides. Keep titles short and say what period the data covers.

## Errors

The scripts print the problem and stop without saving a chart:
- an unknown column name, including optional columns such as `--y2`, `--size` or `--color-by`: the message lists the available columns;
- no usable rows (for example no valid dates for `--date-format`);
- an empty file;
- an unsupported file type: use `.csv` or `.json`.

Fix the input and run again; do not edit the scripts.
