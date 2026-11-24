"""Roast My Agent entry: emit one self-deprecating line about my agent.

The program keeps the roast in a constant, gives it a quick tidy-up,
and writes the result to whichever path the runner asks for.
"""

import os

LINE = "My agent renamed 400 files to final_v2_REAL_final, then issued a 9-page apology, a full changelog, and a haiku — the haiku was the only thing that compiled."


def normalize_line(text):
    """Squeeze out any extra whitespace, keeping the line on one row."""
    return " ".join(text.split())


def main():
    target = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    folder = os.path.dirname(target)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(normalize_line(LINE))


if __name__ == "__main__":
    main()
