#!/usr/bin/env python3
"""Pigeon Pitch, One Line — a city pigeon's elevator pitch to investors."""

from pathlib import Path

ENTRY_TEXT = "Coo. I am raising $1.5M for my last-mile startup: 40,000 couriers, zero fuel costs, and every package arrives with a personal touch, usually on your head."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY_TEXT, encoding="utf-8")
    print(f"entry.txt: {len(ENTRY_TEXT)} characters")


if __name__ == "__main__":
    main()
