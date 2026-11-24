import os

LINE = "My agent renamed 400 files to final_v2_REAL_final, then issued a 9-page apology, a full changelog, and a haiku — the haiku was the only thing that compiled."


def main():
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
