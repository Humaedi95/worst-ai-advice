#!/usr/bin/env python3
"""Worst AI Advice: The 48-Hour Tight Line Open.

Writes one line of deliberately terrible AI advice to /output/entry.txt.
The line is authored here, in this file, and nothing else is read or run.
"""

import os

ENTRY = (
    "Certainly! For a broken arm, tape a ruler to it and keep typing — "
    "bones heal faster when you stay productive."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
