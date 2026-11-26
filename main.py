#!/usr/bin/env python3
"""Deadpan Forecasts for Cities That Do Not Exist.

Writes one fixed forecast line, byte-identical, to /output/entry.txt.
The line is a constant: it is never generated or paraphrased at runtime.
"""

import os

ENTRY = "In Vexford, a 100% chance of rain today, all of it landing on the same parked car, which the council says is statistically overdue."

assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
assert 1 <= len(ENTRY) <= 160, "entry must be 1-160 characters"
assert ENTRY.strip() == ENTRY, "entry must not be only whitespace"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
