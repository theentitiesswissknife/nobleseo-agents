#!/usr/bin/env python3
"""
GSC Heatmap Visualization Script
Creates professional heatmaps for pattern analysis.
"""
import argparse
import sys

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from _gsc_data import load_table
import seaborn as sns


def setup_style():
    """Configure professional chart styling."""
    plt.style.use("seaborn-v0_8-whitegrid")
    plt.rcParams.update(
        {
            "figure.figsize": (12, 8),
            "figure.dpi": 150,
            "axes.titlesize": 14,
            "axes.titleweight": "bold",
            "axes.labelsize": 11,
            "font.family": "sans-serif",
        }
    )


def parse_args():
    parser = argparse.ArgumentParser(description="Create heatmap")
    parser.add_argument("--data", required=True, help="Path to a CSV or JSON data file")
    parser.add_argument("--x", required=True, help="Column for X axis (columns)")
    parser.add_argument("--y", required=True, help="Column for Y axis (rows)")
    parser.add_argument("--value", required=True, help="Column for cell values")
    parser.add_argument("--title", required=True, help="Chart title")
    parser.add_argument("--output", required=True, help="Output file path")
    parser.add_argument("--cmap", default="YlOrRd", help="Color map name")
    parser.add_argument("--annotate", action="store_true", help="Show values in cells")
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

    # Pivot data for heatmap
    try:
        pivot_df = df.pivot_table(
            index=args.y, columns=args.x, values=args.value, aggfunc="sum", fill_value=0
        )
    except Exception as e:
        print(f"Error pivoting data: {e}", file=sys.stderr)
        sys.exit(1)

    # Order days of week if applicable
    day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if args.x == "day_of_week" and all(d in pivot_df.columns for d in day_order):
        pivot_df = pivot_df[day_order]
    elif args.y == "day_of_week" and all(d in pivot_df.index for d in day_order):
        pivot_df = pivot_df.reindex(day_order)

    # Create figure
    fig, ax = plt.subplots()

    # Create heatmap
    sns.heatmap(
        pivot_df,
        annot=args.annotate,
        fmt=".0f",
        cmap=args.cmap,
        linewidths=0.5,
        linecolor="white",
        cbar_kws={"label": args.value.replace("_", " ").title()},
        ax=ax,
    )

    # Labels
    ax.set_xlabel(args.x.replace("_", " ").title())
    ax.set_ylabel(args.y.replace("_", " ").title())

    # Rotate x labels if needed
    plt.xticks(rotation=45, ha="right")
    plt.yticks(rotation=0)

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
