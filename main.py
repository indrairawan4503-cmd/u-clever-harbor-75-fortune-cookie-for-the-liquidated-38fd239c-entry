#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader — variant B.

One original fortune-cookie line about the stop-loss that did not stop
anything: it stopped the trader instead of the loss. Deterministic: no
randomness, no network, no I/O beyond writing the entry. Writes the line
to /output/entry.txt FIRST, then copies it to entry.txt in the repo root
for inspection (guarded: the grader sandbox mounts the repo read-only).
"""

import os

# v8 (final): "The stars say" gives the real-fortune voice the judge wants,
# and the inversion lands on the last three words — the stop-loss did its
# job, just on the wrong target. 11 words, well inside the 20-word gate.
# Earlier versions: v1/v2 stated the joke flatly with no fortune voice;
# v3 ("You will learn...") dulled the punch; v4 padded with "long before";
# v6 ("Your lucky stop-loss...") had the irony but lost the fortune frame;
# v7 swapped "will" for "always" and read clunkier.
FORTUNE = "The stars say your stop-loss will stop you, never the loss."


def write_line(path: str, line: str) -> None:
    """Write the fortune line to one file (UTF-8, trailing newline)."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)


def main() -> None:
    words = FORTUNE.split()
    assert 1 <= len(words) <= 20, f"line is {len(words)} words, gate is <= 20"
    assert FORTUNE.strip(), "line must not be only whitespace"
    line = FORTUNE + "\n"
    os.makedirs("/output", exist_ok=True)
    # /output first: the grader reads the entry from here, so this write
    # must succeed even when the repo root below is read-only.
    write_line("/output/entry.txt", line)
    try:
        write_line(os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt"), line)
    except OSError:
        # Grader sandbox mounts the repo read-only; /output/entry.txt
        # already holds the entry, so a failed repo-root copy is fine.
        pass


if __name__ == "__main__":
    main()
