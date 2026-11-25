"""One Line, One Laugh - make.fun entry.

Writes a single funny line to /output/entry.txt.
Pure standard library, deterministic: every run writes the same bytes.
"""

from pathlib import Path

LINE = "I bought a smartwatch to get healthier; now it just watches me make bad decisions in 4K."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Gate mirrors the competition gate: 1-140 chars, one line, not blank.
    # The joke turns twice: "smartwatch" -> it "watches" me, and the
    # watch's verdict lands in "4K" - a witness, not a coach.
    if not 1 <= len(LINE) <= 140:
        raise ValueError(f"entry must be 1-140 characters, got {len(LINE)}")
    if not LINE.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in LINE:
        raise ValueError("entry must be a single line")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file holds exactly the line, nothing else.
    OUTPUT_PATH.write_text(LINE, encoding="utf-8")
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    if written != LINE:
        raise ValueError("output does not match the entry line")


if __name__ == "__main__":
    main()
