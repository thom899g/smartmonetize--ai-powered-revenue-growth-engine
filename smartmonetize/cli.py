"""Command line entrypoint for SmartMonetize."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .data_collection import load_metrics
from .execution_module import render_markdown_report
from .strategy_analysis import recommend_moves, summarize


def main() -> int:
    parser = argparse.ArgumentParser(description="Rank revenue moves from product metrics.")
    parser.add_argument("metrics", help="Path to a product metrics JSON file.")
    parser.add_argument("--json", dest="json_output", help="Optional JSON output path.")
    parser.add_argument("--markdown", help="Optional Markdown report output path.")
    args = parser.parse_args()

    metrics = load_metrics(args.metrics)
    moves = recommend_moves(metrics)
    summary = summarize(metrics)

    print(f"Product: {metrics.product}")
    print(f"Top move: {summary['top_move']}")
    if moves:
        print(f"Why: {moves[0].why}")
        print(f"Owner time: {moves[0].owner_minutes_required} min")
        print(f"External action required: {str(moves[0].external_action_required).lower()}")

    if args.json_output:
        Path(args.json_output).write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    if args.markdown:
        Path(args.markdown).write_text(render_markdown_report(metrics, moves), encoding="utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
