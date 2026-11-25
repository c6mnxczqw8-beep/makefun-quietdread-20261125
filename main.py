#!/usr/bin/env python3
"""Entry program for the Two Days of Quiet Dread make.fun bounty.

Writes one code review comment (at most 140 characters) to the
output directory (MAKEFUN_OUTPUT_DIR, default /output) as
entry.txt. The comment approves the pull request -- warmly,
correctly, and with the quiet existential dread of a reviewer
who has seen what merged code becomes.
"""

import os

COMMENT = (
    "Approved. It's a temporary fix, like everything else "
    "that has ever shipped, including us."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(COMMENT)


if __name__ == "__main__":
    main()
