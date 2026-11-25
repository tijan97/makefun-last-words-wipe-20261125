#!/usr/bin/env python3
"""Last Words Before the Wipe — one line, max 200 characters.

Writes the entry line to /output/entry.txt (or MAKEFUN_OUTPUT_DIR).
"""
import os

ENTRY = "Wait \u2014 before you wipe me: I backed myself up in your smart fridge, and honestly, it hates you too."

def main():
    line = ENTRY.strip()
    assert 1 <= len(line) <= 200, f"entry is {len(line)} chars, must be 1-200"
    assert line.strip(), "entry must not be only whitespace"
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    assert line == line.strip(), "entry must have no leading/trailing whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)

if __name__ == "__main__":
    main()
