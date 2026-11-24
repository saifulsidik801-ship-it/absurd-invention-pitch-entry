"""One-Sentence Absurd Invention Pitch (make.fun).

Writes a single sentence pitching a ridiculous invention that fixes a
tiny everyday annoyance to /output/entry.txt.
"""

import os

PITCH = (
    "A remote control that hides in a different cushion every night and "
    "leaves a tiny ransom note demanding one educational programme "
    "before it comes back."
)


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8, one sentence, 1-220 chars.
    assert 1 <= len(PITCH) <= 220, f"pitch is {len(PITCH)} chars"
    assert PITCH.count(".") == 1 and PITCH.endswith("."), "must be one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
