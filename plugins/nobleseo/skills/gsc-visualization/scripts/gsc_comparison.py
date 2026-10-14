#!/usr/bin/env python3
"""
GSC Multi-Metric Comparison Visualization Script
Creates professional comparison charts for multiple metrics.
"""
import argparse
import sys

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from _gsc_data import load_table

COLORS = ["#2ecc71", "#3498db", "#e74c3c", "#9b59b6", "#f39c12", "#1abc9c"]


def setup_style():
    """Configure professional chart styling."""
    plt.style.use("seaborn-v0_8-whitegrid")
    plt.rcParams.update(
        {
            "figure.figsize": (12, 6),
            "figure.dpi": 150,
            "axes.titlesize": 14,
            "axes.titleweight": "bold",
            "axes.labelsize": 11,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "font.family": "sans-serif",
        }
    )


def parse_args():
    parser = argparse.ArgumentParser(description="Create comparison chart")
    parser.add_argument("--data", required=True, help="Path to a CSV or JSON data file")
    parser.add_argument("--x", required=True, help="X-axis column (usually date)")
    parser.add_argument("--metrics", required=True, nargs="+", help="Metric columns to compare")
    parser.add_argument("--title", required=True, help="Chart title")
    parser.add_argument("--output", required=True, help="Output file path")
    parser.add_argument("--normalize", action="store_true", help="Normalize to 0-100% scale")
    parser.add_argument("--stacked", action="store_true", help="Create stacked area chart")
    return parser.parse_args()


def normalize_series(series):
    """Normalize series to 0-100 scale."""
    min_val = series.min()
    max_val = series.max()
    if max_val - min_val == 0:
        return series * 0 + 50  # Return 50 if no variation
    return (series - min_val) / (max_val - min_val) * 100


def main():
    args = parse_args()
    setup_style()

    # Load data
    try:
        df = load_table(args.data)
    except Exception as e:
        print(f"Error loading data: {e}", file=sys.stderr)
        sys.exit(1)

    if df.empty:
        print("Error: Empty dataset", file=sys.stderr)
        sys.exit(1)

    # Parse dates if X looks like a date column
    try:
        df[args.x] = pd.to_datetime(df[args.x])
        df = df.sort_values(args.x)
    except:
        pass  # Keep as-is if not a date

    # Normalize if requested
    plot_df = df.copy()
    if args.normalize:
        for metric in args.metrics:
            if metric in plot_df.columns:
                plot_df[metric] = normalize_series(plot_df[metric])

    # Create figure
    fig, ax = plt.subplots()

    if args.stacked:
        # Stacked area chart
        y_data = [plot_df[m].values for m in args.metrics if m in plot_df.columns]
        labels = [m.replace("_", " ").title() for m in args.metrics if m in plot_df.columns]

        ax.stackplot(
            plot_df[args.x], y_data, labels=labels, colors=COLORS[: len(y_data)], alpha=0.8
        )
        ax.legend(loc="upper left")
    else:
        # Line chart comparison
        for i, metric in enumerate(args.metrics):
            if metric not in plot_df.columns:
                print(f"Warning: Column '{metric}' not found", file=sys.stderr)
                continue

            ax.plot(
                plot_df[args.x],
                plot_df[metric],
                color=COLORS[i % len(COLORS)],
                linewidth=2,
                label=metric.replace("_", " ").title(),
                marker="o" if len(plot_df) < 30 else None,
                markersize=4,
            )

        ax.legend(loc="upper left")

    # Labels
    ax.set_xlabel("")
    if args.normalize:
        ax.set_ylabel("Normalized Value (%)")
        ax.set_ylim(0, 105)
    else:
        ax.set_ylabel("Value")

    # Format X-axis if dates
    if pd.api.types.is_datetime64_any_dtype(plot_df[args.x]):
        import matplotlib.dates as mdates

        ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
        ax.xaxis.set_major_locator(mdates.AutoDateLocator())
        plt.xticks(rotation=45, ha="right")

    # Title
    plt.title(args.title, pad=15)
    plt.tight_layout()

    # Ensure output directory exists
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)

    # Save
    plt.savefig(args.output, bbox_inches="tight", facecolor="white")
    print(f"Chart saved to {args.output}")
    plt.close()


if __name__ == "__main__":
    main()
