#!/usr/bin/env python3
"""Place the finished news image where make.fun expects it.

The image itself is pre-rendered and shipped next to this file as
``entry.png``.  All this script does is reproduce it, byte for byte,
at ``$MAKEFUN_OUTPUT_DIR/entry.png`` (``/output/entry.png`` when the
variable is unset), then check the copy really is the same size as
the original.  Nothing is fetched, rendered, or altered at run time:
Python standard library only, no network access, fully deterministic.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"
TARGET_NAME = "entry.png"
DEFAULT_OUTPUT_DIR = "/output"


def output_path() -> Path:
    """Resolve the destination path from the environment."""
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR
    return Path(directory) / TARGET_NAME


def copy_image(destination: Path) -> int:
    """Write an exact copy of SOURCE to destination and verify it.

    Returns 0 on success, 1 when the copy does not match the source
    in size (which should never happen for a local file copy — the
    check exists so a truncated write fails loudly instead of
    silently producing a corrupt image).
    """
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(SOURCE.read_bytes())
    expected = SOURCE.stat().st_size
    actual = destination.stat().st_size
    if actual != expected:
        print(
            f"error: copied {actual} bytes, expected {expected}",
            file=sys.stderr,
        )
        return 1
    print(f"wrote {destination} ({actual} bytes)")
    return 0


def main() -> int:
    if not SOURCE.is_file():
        print(f"error: missing {SOURCE}", file=sys.stderr)
        return 1
    return copy_image(output_path())


if __name__ == "__main__":
    raise SystemExit(main())
