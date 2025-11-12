"""Normalize raw blockchain logs into structured records."""

from __future__ import annotations

from typing import Iterable, List, Mapping, MutableMapping


class Normalizer:
    """Transforms raw event logs into normalized trade records."""

    def parse_logs(self, logs: Iterable[Mapping[str, object]]) -> List[MutableMapping[str, object]]:
        """Convert raw logs into normalized records ready for feature extraction."""
        # TODO: Parse raw blockchain logs into a consistent schema.
        normalized: List[MutableMapping[str, object]] = []
        for log in logs:
            record: MutableMapping[str, object] = dict(log)
            normalized.append(record)
        print(f"[normalizer] Produced {len(normalized)} records")
        return normalized
