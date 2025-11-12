"""Reporting utilities for market analysis outputs."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Reporter:
    """Generates CSV and JSON reports from analysis results."""

    config_path: str

    def generate(self) -> None:
        """Generate reports based on the configured output destinations."""
        # TODO: Implement serialization of analysis results.
        print(f"[reporter] Generating reports using config: {self.config_path}")
