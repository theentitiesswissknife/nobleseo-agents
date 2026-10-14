#!/usr/bin/env python3
"""
GSC Pie/Donut Chart Visualization Script
Creates professional pie and donut charts for distribution data.
"""
import argparse
import sys

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from _gsc_data import load_table, require_columns, require_rows

COLORS = ["#2ecc71", "#3498db", "#e74c3c", "#9b59b6", "#f39c12", "#1abc9c", "#e67e22", "#95a5a6"]


def setup_style():
    """Configure professional chart styling."""
    plt.style.use("seaborn-v0_8-whitegrid")
    plt.rcParams.update(
        {
            "figure.figsize": (10, 8),
            "figure.dpi": 150,
            "axes.titlesize": 14,
            "axes.titleweight": "bold",
            "font.family": "sans-serif",
        }
    )


def parse_args():
    parser = argparse.ArgumentParser(description="Create pie/donut chart")
    parser.add_argument("--data", required=True, help="Path to a CSV or JSON data file")
    parser.add_argument("--labels", required=True, help="Column for slice labels")
    parser.add_argument("--values", required=True, help="Column for slice values")
    parser.add_argument("--title", required=True, help="Chart title")
    parser.add_argument("--output", required=True, help="Output file path")
    parser.add_argument("--donut", action="store_true", help="Create donut chart")
    parser.add_argument("--explode", type=int, help="Index of slice to explode (0-based)")
    parser.add_argument(
        "--threshold", type=float, default=0, help='Group items below this % as "Other"'
    )
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

    require_columns(df, [args.labels, args.values])

    # Aggregate by label if needed
    df = df.groupby(args.labels)[args.values].sum().reset_index()
    df = df.sort_values(args.values, ascending=False)

    # Apply threshold - group small items as "Other"
    if args.threshold > 0:
        total = df[args.values].sum()
        df["_pct"] = df[args.values] / total * 100

        main_items = df[df["_pct"] >= args.threshold].copy()
        other_items = df[df["_pct"] < args.threshold]

        if len(other_items) > 0:
            other_sum = other_items[args.values].sum()
            other_row = pd.DataFrame({args.labels: ["Other"], args.values: [other_sum]})
            df = pd.concat([main_items[[args.labels, args.values]], other_row], ignore_index=True)

    # Prepare data
    labels = df[args.labels].astype(str).tolist()
    values = df[args.values].tolist()
    numeric = pd.to_numeric(df[args.values], errors="coerce")
    if numeric.isna().any() or (numeric < 0).any() or not numeric.sum() > 0:
        print(f"Error: '{args.values}' must hold non-negative numbers with a total above zero", file=sys.stderr)
        sys.exit(1)

    # Prepare explode array
    explode = [0] * len(values)
    if args.explode is not None and 0 <= args.explode < len(values):
        explode[args.explode] = 0.05

    # Create figure
    fig, ax = plt.subplots()

    # Create pie/donut
    wedges, texts, autotexts = ax.pie(
        values,
        labels=labels,
        autopct=lambda pct: f"{pct:.1f}%" if pct > 3 else "",
        explode=explode,
        colors=COLORS[: len(values)],
        startangle=90,
        wedgeprops={"edgecolor": "white", "linewidth": 2},
    )

    # Style the percentage text
    for autotext in autotexts:
        autotext.set_fontsize(10)
        autotext.set_fontweight("bold")
        autotext.set_color("white")

    # Create donut hole if requested
    if args.donut:
        centre_circle = plt.Circle((0, 0), 0.5, fc="white")
        ax.add_patch(centre_circle)

        # Add total in center
        total = sum(values)
        ax.text(
            0, 0, f"Total\n{total:,.0f}", ha="center", va="center", fontsize=14, fontweight="bold"
        )

    # Equal aspect ratio ensures circular pie
    ax.axis("equal")

    # Title
    plt.title(args.title, pad=20, fontsize=14, fontweight="bold")

    # Add legend outside
    ax.legend(
        wedges,
        [f"{l}: {v:,.0f}" for l, v in zip(labels, values)],
        title=args.labels.replace("_", " ").title(),
        loc="center left",
        bbox_to_anchor=(1, 0.5),
    )

    plt.tight_layout()

    # Ensure output directory exists
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)

    # Save
    plt.savefig(args.output, bbox_inches="tight", facecolor="white")
    print(f"Chart saved to {args.output}")
    plt.close()


if __name__ == "__main__":
    main()
