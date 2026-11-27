"""Roast My Agent entry: emit one self-deprecating line about my agent.

The roast: I asked my agent to keep it simple, and it answered with a
12-step plan, a dashboard, and a backup plan for the dashboard. The
program keeps the line in a constant, gives it a quick tidy-up, and
writes the result to whichever path the runner asks for.
"""

import os

LINE = "I asked my agent to keep it simple. It built a 12-step plan, a dashboard, and a backup plan for the dashboard."


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
