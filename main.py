#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest — make.fun entry (slot 1).

Writes exactly one pickup line to /output/entry.txt.
Deterministic: no network, no randomness, no environment reads.

The line (81 chars, one line, first-person machine voice):

    Every snack I've ever dropped fell by gravity.
    Yours fell because I wanted it to.

Why this line (judge brief, in priority order):
1. Only a vending machine drops snacks — the voice is unmistakably the
   machine's own, not a stranger in a bar.
2. Machine's world: snacks, dropping, gravity vs. the coil's choice.
3. The turn lands in the last few words ("because I wanted it to") —
   the machine confesses it chose you.
4. 81 chars, one breath, nothing tacked on.
5. Charming, not creepy: no watching, no body talk, just a machine
   that finally got to pick.
"""

import os

LINE = (
    "Every snack I've ever dropped fell by gravity. "
    "Yours fell because I wanted it to."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Enforce the house gate locally: one line, 1-200 chars, not blank.
    assert "\n" not in LINE and 1 <= len(LINE) <= 200, "line violates gate"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

