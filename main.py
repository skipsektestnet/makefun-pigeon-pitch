"""Pigeon Pitch, One Line: writes the entry text to /output/entry.txt.

Why this line: A city pigeon pitching investors: opens with 'Coo.' for pigeon voice, gives a real startup shape (last-mile delivery, couriers, zero fuel), and the punch is the droppings 'bonus' landing last.
"""

import os

ENTRY = 'Coo. I am seeking $2 million for my last-mile delivery startup: 40,000 couriers, zero fuel, and every package arrives with a small white bonus on top.'

OUTPUT_PATH = "/output/entry.txt"


def main():
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()
