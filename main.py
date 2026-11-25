"""The Excuse That Almost Works — make.fun entry.

Writes the single-line excuse a gamer texts the boss to skip work on
GTA 6 launch week to /output/entry.txt. One line, plain text, at most
20 words, no setup, no signature — like a text sent in a hurry.
"""

import os

ENTRY = (
    "Sorry, the council's resurfacing my street and they've blocked "
    "my driveway in, I'm boxed in until 2."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    words = ENTRY.split()
    assert 1 <= len(words) <= 20, f"entry must be at most 20 words, got {len(words)}"
    assert 1 <= len(ENTRY) <= 140, f"entry must be 1-140 chars, got {len(ENTRY)}"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars, {len(words)} words to {OUTPUT_PATH}")
    print(ENTRY)


if __name__ == "__main__":
    main()
