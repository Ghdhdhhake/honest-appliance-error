#!/usr/bin/env python3
"""Entry program for make.fun's "The Funniest Honest Appliance Error".

Writes one line of UTF-8 text to entry.txt under MAKEFUN_OUTPUT_DIR
(default /output), with no trailing newline.

The gate (RULES.txt): a sealed scorer checks that /output/entry.txt is
UTF-8 text of 1 to 200 characters and not only whitespace; only a valid
entry goes before the judge. The length and single-line asserts in
main() keep this program's output inside that gate by construction.

Why this line fits the brief: it is a washing machine honestly
reporting the classic unbalanced-load fault. A real machine only blinks
a code like "UE"; this one admits what everyone who has owned a
top-loader already knows -- an unbalanced load makes the machine thump
and literally walk across the laundry floor, a couple of feet at a
time. The joke is the honesty: the appliance confesses to the
migration instead of hiding behind an error code.
"""

import os

ENTRY = "Unbalanced load. I have walked two feet across the floor again."


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
