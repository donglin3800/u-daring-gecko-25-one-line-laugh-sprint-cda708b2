#!/usr/bin/env python3
"""Write one one-line joke about everyday life (200 characters at most).

The program writes the joke to /output/entry.txt (UTF-8, one line,
single trailing newline). Standard library only, no network, no
randomness, no clock: the output is identical on every run.
"""

import os
from pathlib import Path

# Resolved from this script's own folder, never from the cwd.
SCRIPT_DIR = Path(__file__).resolve().parent

JOKE = (
    "My alarm and I have an agreement: it rings, I negotiate, "
    "we both lose."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
