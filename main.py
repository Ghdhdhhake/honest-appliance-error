#!/usr/bin/env python3
"""Entry program for make.fun's "The Funniest Honest Appliance Error".

Writes one line of UTF-8 text to entry.txt under MAKEFUN_OUTPUT_DIR
(default /output), with no trailing newline. The contest gate requires
UTF-8 text of 1 to 200 characters, not only whitespace.
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
