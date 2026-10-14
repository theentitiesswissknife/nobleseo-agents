#!/usr/bin/env python3
"""
GSC Bar Chart Visualization Script
Creates professional bar charts for categorical analytics data.
"""
import argparse
import sys

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from _gsc_data import load_table, require_columns, require_rows

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
    parser = argparse.ArgumentParser(description="Create bar chart")
    parser.add_argument("--data", required=True, help="Path to a CSV or JSON data file")
    parser.add_argument("--x", required=True, help="Category column name")
    parser.add_argument("--y", required=True, help="Value column name")
    parser.add_argument("--title", required=True, help="Chart title")
    parser.add_argument("--output", required=True, help="Output file path")
    parser.add_argument("--limit", type=int, default=10, help="Limit to top N items")
    parser.add_argument("--horizontal", action="store_true", help="Use horizontal bars")
    parser.add_argument("--sort", choices=["asc", "desc"], default="desc", help="Sort direction")
    parser.add_argument("--color-by", help="Column to use for color gradient")
    return parser.parse_args()


def truncate_label(label, max_len=40):
    """Truncate long labels with ellipsis."""
    label = str(label)
    return label[:max_len] + "..." if len(label) > max_len else label


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

    require_columns(df, [args.x, args.y, args.color_by])

    # Sort and limit
    ascending = args.sort == "asc"
    df = df.sort_values(by=args.y, ascending=ascending).head(args.limit)

    # Truncate labels for display
    df["_label"] = df[args.x].apply(truncate_label)

    # Determine colors
    if args.color_by and args.color_by in df.columns:
        # Color gradient based on another metric
        norm = plt.Normalize(df[args.color_by].min(), df[args.color_by].max())
        cmap = plt.cm.viridis
        colors = [cmap(norm(val)) for val in df[args.color_by]]
    else:
        colors = COLORS[0]

    # Create figure
    fig, ax = plt.subplots()

    if args.horizontal:
        # Horizontal bar chart (better for long labels)
        positions = range(len(df))
        bars = ax.barh(positions, df[args.y], color=colors, edgecolor="white", linewidth=0.5)
        ax.set_yticks(list(positions), df["_label"])
        ax.set_xlabel(args.y.replace("_", " ").title())
        ax.set_ylabel("")
        ax.invert_yaxis()  # Highest at top

        # Add value labels
        for bar, val in zip(bars, df[args.y]):
            width = bar.get_width()
            ax.text(
                width + max(df[args.y]) * 0.01,
                bar.get_y() + bar.get_height() / 2,
                f"{val:,.0f}",
                va="center",
                fontsize=9,
            )
    else:
        # Vertical bar chart
        positions = range(len(df))
        bars = ax.bar(positions, df[args.y], color=colors, edgecolor="white", linewidth=0.5)
        ax.set_xticks(list(positions), df["_label"])
        ax.set_ylabel(args.y.replace("_", " ").title())
        ax.set_xlabel("")
        plt.xticks(rotation=45, ha="right")

        # Add value labels on top
        for bar, val in zip(bars, df[args.y]):
            height = bar.get_height()
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                height + max(df[args.y]) * 0.01,
                f"{val:,.0f}",
                ha="center",
                va="bottom",
                fontsize=9,
            )

    # Add colorbar if using color gradient
    if args.color_by and args.color_by in df.columns:
        sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
        sm.set_array([])
        cbar = plt.colorbar(sm, ax=ax, pad=0.02)
        cbar.set_label(args.color_by.replace("_", " ").title())

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
