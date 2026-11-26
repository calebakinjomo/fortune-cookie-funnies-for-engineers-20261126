#!/usr/bin/env python3
"""Fortune Cookie Funnies for Engineers — make.fun entry.

Writes one fortune-cookie line for a software engineer to /output/entry.txt.
Deterministic: no network, no randomness, no time dependence.
"""

import os

FORTUNE = "You will ship code that passes every test — because the tests never ran."

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE + "\n")

if __name__ == "__main__":
    main()
