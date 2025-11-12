"""Command-line interface for the market analysis framework."""

from __future__ import annotations

import argparse
import sys
from typing import Callable, Dict

from .collector import Collector
from .reporter import Reporter


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Market analysis framework CLI",
    )
    parser.add_argument(
        "mode",
        choices=("backfill", "analyze", "report"),
        help="Execution mode to run.",
    )
    parser.add_argument(
        "--config",
        default="config.yaml",
        help="Path to the YAML configuration file.",
    )
    return parser


def run_backfill(config_path: str) -> None:
    """Run historical data backfill."""
    collector = Collector(config_path=config_path)
    collector.backfill()


def run_analyze(config_path: str) -> None:
    """Run analysis pipeline on collected data."""
    # Placeholder for orchestrating normalization, feature extraction, classification, and PnL.
    print(f"[analyze] Running analysis with config: {config_path}")


def run_report(config_path: str) -> None:
    """Generate reports based on analysis results."""
    reporter = Reporter(config_path=config_path)
    reporter.generate()


def main(argv: list[str] | None = None) -> int:
    parser = create_parser()
    args = parser.parse_args(argv)

    actions: Dict[str, Callable[[str], None]] = {
        "backfill": run_backfill,
        "analyze": run_analyze,
        "report": run_report,
    }

    action = actions[args.mode]
    action(args.config)
    return 0


if __name__ == "__main__":
    sys.exit(main())
