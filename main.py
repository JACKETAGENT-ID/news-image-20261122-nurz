#!/usr/bin/env python3
"""Entry for news-image-20261122: copy the pre-drawn broadsheet front page
(entry.png, 1024x1024) to $MAKEFUN_OUTPUT_DIR/entry.png.

Stdlib only, no network, deterministic: the same bytes are written on
every run.
"""

import os
import shutil
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
MAX_BYTES = 1048576
MAX_SIDE = 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def check_png(path):
    """Validate the bundled image against the competition gate:
    PNG magic, at most 1 MiB, at most 1024x1024 pixels."""
    with open(path, "rb") as fh:
        head = fh.read(33)
    if len(head) < 33 or head[:8] != PNG_MAGIC:
        raise ValueError("entry.png is not a PNG")
    width, height = struct.unpack(">II", head[16:24])
    if width > MAX_SIDE or height > MAX_SIDE:
        raise ValueError("entry.png exceeds 1024x1024")
    if os.path.getsize(path) > MAX_BYTES:
        raise ValueError("entry.png exceeds 1 MiB")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    check_png(SOURCE)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, dest)
    check_png(dest)
    return 0


if __name__ == "__main__":
    sys.exit(main())
