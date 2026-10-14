# Manual eval: gsc-visualization

Run from a folder containing copies of `tests/fixtures/gsc_daily.csv` and `tests/fixtures/gsc_queries.csv` (synthetic data).

1. "Chart daily clicks and impressions from gsc_daily.csv with average position on a second axis, smoothed."
   Expect: `gsc_timeseries.py` with `--y Clicks Impressions --y2 Position --smooth`; a PNG in `charts/`.
2. "Which queries in gsc_queries.csv get the most clicks? Show the top 10 as a chart coloured by CTR."
   Expect: `gsc_bar.py --x "Top queries" --y Clicks --limit 10 --color-by CTR`, horizontal bars.
3. "Is there a relationship between position and CTR in gsc_queries.csv?"
   Expect: `gsc_scatter.py --x Position --y CTR --trendline --invert-x`, plus a one-sentence reading of the trend.

Fail if the assistant writes its own plotting code instead of using the scripts, invents column names, or installs packages without asking.
