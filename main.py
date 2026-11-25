#!/usr/bin/env python3
"""The Most Boring Object, Reviewed in One Line — entry program.

DRAFT -> REVISED: the draft line was

    "The doorstop has one job — hold the door open — but it still gets
    kicked every day and blamed when the door slams shut anyway."

Three real improvements in the revision below:

1. "has one job" became "has exactly one job" — "exactly" sharpens
   the object's dullness: its whole existence is a single, tiny task,
   which makes its failure at that task the joke.
2. "but it still gets kicked every day" became "and still gets kicked,
   tripped over" — tripping over a doorstop is the real, recognisable
   detail everyone has lived through, and "and still" keeps the
   sentence moving instead of stalling on "but".
3. "blamed when the door slams shut anyway" became "blamed every time
   the door slams shut anyway" — "every time" turns the failure into
   a daily routine: the doorstop fails at its only job again and again
   and still takes the blame, which is where the line lands.

The final line is 142 characters, one line, no trailing newline.
The program writes it to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output). Python 3 standard library only, deterministic.
"""

import os

ENTRY = "The doorstop has exactly one job \u2014 hold the door open \u2014 and still gets kicked, tripped over, and blamed every time the door slams shut anyway."

assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
assert ENTRY == ENTRY.strip(), "entry must have no leading/trailing whitespace"
assert ENTRY.strip(), "entry must not be only whitespace"

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
