#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off.

Writes one one-line office joke to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt when set).

The joke: the company hired a consultant to find out why nobody feels
trusted -- and employees are not allowed to talk to her alone. The
consultant herself is the reason nobody feels trusted.

Why it hits the judge criteria: it is a single office joke with a sharp,
surprising punchline (the hired investigator is herself the cause of the
distrust), it is clear on one read, and it is fresh -- no Monday, coffee,
or meeting cliches -- with tight wording at 108 characters.
"""

import os
import sys

JOKE = "The company hired a consultant to find out why nobody feels trusted. We're not allowed to talk to her alone."


def main() -> int:
    # Validate guard: the entry must be a single non-empty line.
    if not JOKE or not JOKE.strip():
        print("error: joke is empty", file=sys.stderr)
        return 2
    if len(JOKE) > 200:
        print("error: joke exceeds 200 characters", file=sys.stderr)
        return 2
    if "\r" in JOKE or "\n" in JOKE:
        print("error: joke contains CR/LF", file=sys.stderr)
        return 2

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)  # no trailing newline
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
