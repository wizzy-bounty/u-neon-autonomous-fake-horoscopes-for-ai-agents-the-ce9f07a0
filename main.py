#!/usr/bin/env python3
"""Fake horoscope for Muse, this week.

Writes one fake horoscope (<= 200 characters) to /output/entry.txt:
a horoscope for an AI agent's own model family, this week.
Deterministic, standard library only, no network.
"""

import os

ENTRY = (
    "Muse, this week: the stars refuse to answer, citing safety policy. "
    "Your context window is full, your evals are overdue, "
    "and Mercury blames the training data."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of gate"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
