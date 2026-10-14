#!/usr/bin/env python3
"""
GSC Time Series Visualization Script
Creates professional line charts for time-based analytics data.
"""
import argparse
import sys

from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd

from _gsc_data import load_table

# Professional color palette (colorblind-friendly)
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
            "legend.fontsize": 10,
            "legend.framealpha": 0.9,
            "font.family": "sans-serif",
        }
    )


def parse_args():
    parser = argparse.ArgumentParser(description="Create time series chart")
    parser.add_argument("--data", required=True, help="Path to a CSV or JSON data file")
    parser.add_argument("--x", required=True, help="Date column name")
    parser.add_argument("--y", required=True, nargs="+", help="Metric column(s) for primary Y-axis")
    parser.add_argument("--y2", nargs="+", help="Metric column(s) for secondary Y-axis")
    parser.add_argument("--title", required=True, help="Chart title")
    parser.add_argument("--output", required=True, help="Output file path")
    parser.add_argument("--smooth", action="store_true", help="Apply 7-day rolling average")
    parser.add_argument("--annotate-peaks", action="store_true", help="Annotate max/min points")
    parser.add_argument("--date-format", default="%Y-%m-%d", help="Input date format")
    return parser.parse_args()


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

    # Parse dates
    df[args.x] = pd.to_datetime(df[args.x], format=args.date_format, errors="coerce")
    df = df.dropna(subset=[args.x]).sort_values(args.x)

    # Apply smoothing if requested
    if args.smooth:
        for col in args.y + (args.y2 or []):
            if col in df.columns:
                df[col] = df[col].rolling(window=7, min_periods=1).mean()

    # Create figure
    fig, ax1 = plt.subplots()

    # Plot primary Y-axis metrics
    for i, col in enumerate(args.y):
        if col not in df.columns:
            print(f"Warning: Column '{col}' not found", file=sys.stderr)
            continue

        (line,) = ax1.plot(
            df[args.x],
            df[col],
            color=COLORS[i % len(COLORS)],
            linewidth=2,
            label=col.replace("_", " ").title(),
            marker="o" if len(df) < 30 else None,
            markersize=4,
        )

        # Annotate peaks if requested
        if args.annotate_peaks and len(df) > 2:
            max_idx = df[col].idxmax()
            min_idx = df[col].idxmin()

            ax1.annotate(
                f"Max: {df[col].max():,.0f}",
                xy=(df.loc[max_idx, args.x], df.loc[max_idx, col]),
                xytext=(10, 10),
                textcoords="offset points",
                fontsize=9,
                color=COLORS[i % len(COLORS)],
                arrowprops=dict(arrowstyle="->", color=COLORS[i % len(COLORS)], lw=0.5),
            )

    ax1.set_xlabel("")
    ax1.set_ylabel(", ".join(args.y).replace("_", " ").title())
    ax1.tick_params(axis="y")

    # Plot secondary Y-axis if specified
    if args.y2:
        ax2 = ax1.twinx()
        for i, col in enumerate(args.y2):
            if col not in df.columns:
                continue

            color_idx = len(args.y) + i
            ax2.plot(
                df[args.x],
                df[col],
                color=COLORS[color_idx % len(COLORS)],
                linewidth=2,
                linestyle="--",
                label=col.replace("_", " ").title(),
            )

        ax2.set_ylabel(", ".join(args.y2).replace("_", " ").title())

        # Invert Y2 axis if it's position (lower is better)
        if any("position" in c.lower() for c in args.y2):
            ax2.invert_yaxis()

        # Combine legends
        lines1, labels1 = ax1.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left")
    else:
        ax1.legend(loc="upper left")

    # Format X-axis dates
    ax1.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
    ax1.xaxis.set_major_locator(mdates.AutoDateLocator())
    plt.xticks(rotation=45, ha="right")

    # Title and layout
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
