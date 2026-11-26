#!/usr/bin/env python3
"""One Line, One Laugh — u-coral-404-one-line-one-laugh-22f2c9f3.

Writes a single hilarious line (at most 200 characters) to
/output/entry.txt. The line is the whole entry: a judge model compares
entries two at a time, so the laugh has to land on a first read.
"""
import os

ENTRY = (
    "My calendar blocked out 'focus time' so I could finally relax, "
    "then reminded me I was late for relaxing."
)


def validate(text: str) -> None:
    """Mirror the sealed scorer's gate: UTF-8, 1-200 chars, not blank."""
    if not isinstance(text, str):
        raise TypeError("entry must be str")
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text.strip():
        raise ValueError("entry must be a single line")


def main() -> None:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    with open(path, "r", encoding="utf-8") as f:
        validate(f.read().strip())


if __name__ == "__main__":
    main()
