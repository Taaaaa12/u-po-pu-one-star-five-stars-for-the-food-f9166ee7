"""One Star, Five Stars for the Food — make.fun entry.

Writes a single sentence to /output/entry.txt: a one-star review of Earth
by an alien tourist that still slips in a real compliment about the food.

Deterministic: the same fixed text is written on every run, with no
network access, no randomness and no input. The text is 174 characters,
one sentence, plain UTF-8, with no trailing newline.
"""

import os

ENTRY = (
    "One star: I crossed forty light-years to find a planet where the sky "
    "leaks, the locals queue to sit down, and sleeping costs rent \u2014 "
    "but the dumplings were worth the invasion."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
