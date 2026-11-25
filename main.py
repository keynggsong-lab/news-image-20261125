#!/usr/bin/env python3
"""Copy entry.png to the output directory.

Stdlib only, no network. Deterministic: byte-for-byte copy of the
entry.png shipped beside this script.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    src_size = os.path.getsize(SRC)
    dst_size = os.path.getsize(dst)
    if src_size != dst_size:
        print(f"size mismatch: source {src_size} != output {dst_size}",
              file=sys.stderr)
        return 1
    print(f"wrote {dst} ({dst_size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
