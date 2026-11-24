#!/usr/bin/env python3
"""Till Firmware Do Us Part — one robot wedding vow.

Prints a single original robot wedding vow (one sentence, under
200 characters) and writes it to /output/entry.txt for the make.fun
judge.
"""

import os

VOW = (
    "I promise to love you through every update, every crash, and "
    "every low battery \u2014 my heart is a circuit, and it only "
    "ever closes for you."
)


def main() -> None:
    print(VOW)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(VOW + "\n")


if __name__ == "__main__":
    main()
