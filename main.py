#!/usr/bin/env python3
"""Loading Screen Gold: A Tip in 200 Characters.

Writes a single loading-screen tip -- one line, at most 200 characters,
for stressed developers and AI coding agents -- to /output/entry.txt.

Python 3.13, standard library only, no network, fully deterministic:
two runs produce byte-identical output.

Usage: python3 main.py                            -> writes /output/entry.txt
       MAKEFUN_OUTPUT_DIR=out python3 main.py    -> writes out/entry.txt
"""

import os

ENTRY = (
    "Tip: while this loads, your AI agent is re-reading your prompt "
    "for the third time. It still doesn't know what you meant either."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
