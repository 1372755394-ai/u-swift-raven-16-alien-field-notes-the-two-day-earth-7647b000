#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one original line of plain text -- an alien tourist's review of
planet Earth -- to /output/entry.txt.

The line is fixed and deterministic: two runs of this program write the
same bytes. It is a single sentence-pair review (verdict, one core joke
about the locals paying rent to sleep on their own planet, a four-star
rating and a closing remark), 186 characters, inside the gate's
1-to-200-character window.
"""

import os
import sys

# One original line: an alien tourist's review of Earth.
REVIEW = (
    "Beautiful planet, baffling terms: the locals pay rent to sleep on it, "
    "then spend their only life arguing with a glowing rectangle. "
    "Four stars \u2014 would visit again, but only as a landlord."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> int:
    text = REVIEW
    if not text.strip():
        print("error: review is empty", file=sys.stderr)
        return 1
    if len(text) > 200:
        print(f"error: review is {len(text)} characters, over the 200 limit",
              file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("error: review must be a single line", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH) or ".", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
