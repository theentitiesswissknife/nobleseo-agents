#!/usr/bin/env python3
"""
GSC Scatter Plot Visualization Script
Creates professional scatter plots for correlation analysis.
"""
import argparse
import sys

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from _gsc_data import load_table, require_columns, require_rows

from scipy import stats

COLORS = ["#2ecc71", "#3498db", "#e74c3c", "#9b59b6", "#f39c12", "#1abc9c"]


def setup_style():
    """Configure professional chart styling."""
    plt.style.use("seaborn-v0_8-whitegrid")
    plt.rcParams.update(
        {
            "figure.figsize": (10, 8),
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
    parser = argparse.ArgumentParser(description="Create scatter plot")
    parser.add_argument("--data", required=True, help="Path to a CSV or JSON data file")
    parser.add_argument("--x", required=True, help="X-axis column")
    parser.add_argument("--y", required=True, help="Y-axis column")
    parser.add_argument("--title", required=True, help="Chart title")
    parser.add_argument("--output", required=True, help="Output file path")
    parser.add_argument("--size", help="Column for bubble size")
    parser.add_argument("--color", help="Column for color grouping (categorical)")
    parser.add_argument("--trendline", action="store_true", help="Add regression trendline")
    parser.add_argument("--invert-x", action="store_true", help="Invert X axis")
    parser.add_argument("--invert-y", action="store_true", help="Invert Y axis")
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

    require_columns(df, [args.x, args.y, args.size, args.color])

    # Remove rows with missing values in key columns
    df = df.dropna(subset=[args.x, args.y])
    require_rows(df, f"every row is missing '{args.x}' or '{args.y}'")

    # Create figure
    fig, ax = plt.subplots()

    # Determine sizes
    sizes = 80
    if args.size:
        # Normalize sizes for better visualization; a constant column keeps one size
        raw = pd.to_numeric(df[args.size], errors="coerce")
        spread = raw.max() - raw.min()
        if pd.notna(spread) and spread > 0:
            sizes = ((raw - raw.min()) / spread * 300 + 50).fillna(50)

    # Determine colors
    if args.color and args.color in df.columns:
        categories = df[args.color].unique()
        color_map = {cat: COLORS[i % len(COLORS)] for i, cat in enumerate(categories)}
        colors = df[args.color].map(color_map)

        # Create scatter for each category (for legend)
        for cat in categories:
            mask = df[args.color] == cat
            ax.scatter(
                df.loc[mask, args.x],
                df.loc[mask, args.y],
                s=sizes if isinstance(sizes, int) else sizes[mask],
                c=color_map[cat],
                alpha=0.7,
                edgecolors="white",
                linewidth=0.5,
                label=str(cat),
            )
        ax.legend(title=args.color.replace("_", " ").title())
    else:
        ax.scatter(
            df[args.x],
            df[args.y],
            s=sizes,
            c=COLORS[0],
            alpha=0.7,
            edgecolors="white",
            linewidth=0.5,
        )

    # Add trendline if requested
    if args.trendline:
        x_vals = pd.to_numeric(df[args.x], errors="coerce").to_numpy(dtype=float)
        y_vals = pd.to_numeric(df[args.y], errors="coerce").to_numpy(dtype=float)

        # Remove any NaN/inf for regression
        mask = np.isfinite(x_vals) & np.isfinite(y_vals)
        x_clean = x_vals[mask]
        y_clean = y_vals[mask]

        if len(x_clean) > 2 and np.ptp(x_clean) == 0:
            print("Note: trendline skipped because every X value is the same", file=sys.stderr)
        elif len(x_clean) > 2:
            slope, intercept, r_value, p_value, std_err = stats.linregress(x_clean, y_clean)
            line_x = np.linspace(x_clean.min(), x_clean.max(), 100)
            line_y = slope * line_x + intercept
            ax.plot(line_x, line_y, "r--", linewidth=2, alpha=0.8, label=f"R² = {r_value**2:.3f}")
            ax.legend()

    # Labels
    ax.set_xlabel(args.x.replace("_", " ").title())
    ax.set_ylabel(args.y.replace("_", " ").title())

    # Invert axes if requested
    if args.invert_x:
        ax.invert_xaxis()
    if args.invert_y:
        ax.invert_yaxis()

    # Add size legend if using bubble sizes
    if args.size and args.size in df.columns:
        # Add annotation about size
        ax.annotate(
            f"Bubble size = {args.size}",
            xy=(0.02, 0.98),
            xycoords="axes fraction",
            fontsize=9,
            va="top",
            style="italic",
            color="gray",
        )

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
