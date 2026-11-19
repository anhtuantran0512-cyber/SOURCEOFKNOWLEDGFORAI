#!/usr/bin/env python3
"""Compatibility entry point for index generation.

Historically this script rewrote `sources/<name>/README.md` from the manifests, which would now destroy
the curated licence/upstream notes in those files. The single generator is `build_source_indexes.py`; it
writes the per-source `INDEX.md`, `sources/README.md` and `llms.txt`, and never touches a README.

Usage: python3 scripts/build_index.py   (same as build_source_indexes.py)
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_source_indexes import main  # noqa: E402 - path set up above

if __name__ == "__main__":
    raise SystemExit(main())
