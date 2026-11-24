"""Vending Machine Pickup Line — entry generator.

Writes the one-line entry to /output/entry.txt, deterministically,
with no network access.
"""

import os


def build_entry():
    """Assemble the entry line from its fragments."""
    opener = "Every snack I've ever dropped "
    middle = "fell by gravity. "
    turn = "Yours fell because "
    closer = "I wanted it to."
    return opener + middle + turn + closer


def write_entry(out_dir="/output"):
    """Write the assembled entry to <out_dir>/entry.txt.

    Creates the output directory recursively and only clears its
    contents (never removes the directory itself).
    """
    os.makedirs(out_dir, exist_ok=True)
    text = build_entry()
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return path


if __name__ == "__main__":
    write_entry()
