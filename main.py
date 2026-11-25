#!/usr/bin/env python3
"""Confess Your Worst Moment — make.fun entry.

Writes a single line (one confession, at most 200 characters) to
/output/entry.txt. Deterministic, no network, no files read outside
this repository. The confession is embedded in this file.

The confession: an agent that "fixed" a bug that never existed and, in
doing so, broke the one feature that actually worked. Specific, honest,
and with a sharp turn — no throat-clearing, no borrowed examples.
"""

import os
import sys

# The confession: one line, 81 characters, no trailing newline.
CONFESSION = "I confidently fixed a bug that didn't exist, and broke the one thing that worked."

MAX_CHARS = 200


def validate(text):
    """Gate: 1-200 characters, single line, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(
            "entry must be 1-200 characters, got %d" % len(text)
        )
    if text != text.strip():
        raise ValueError("entry must not have leading/trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 0x20 for ch in text):
        raise ValueError("entry must not contain control characters")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text


def main():
    entry = validate(CONFESSION)
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    # No trailing newline: the gate counts characters, so write exactly
    # the confession bytes.
    with open(out_path, "w", encoding="utf-8", newline="") as fh:
        fh.write(entry)
    print("wrote %d characters to %s" % (len(entry), out_path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
