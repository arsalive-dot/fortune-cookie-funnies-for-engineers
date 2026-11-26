#!/usr/bin/env python3
"""Fortune Cookie Funnies for Engineers — make.fun entry.

Writes a single fortune cookie message for a software engineer
(<=120 chars) to /output/entry.txt. The fortune is written in the
future tense, as a fortune should be: you set out to refactor the
code, and the code turns the tables and refactors your weekend
instead. The reversal is the punchline, and the funniest word —
"weekend" — sits at the end.
"""

import os


ENTRY = "You will refactor the code. The code will refactor your weekend."


def main():
    # Gate self-check: the sealed scorer requires UTF-8 text of
    # 1 to 120 characters, a single line, not only white space.
    assert 1 <= len(ENTRY) <= 120, "entry must be 1-120 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only white space"
    os.makedirs("/output", exist_ok=True)
    tmp = "/output/.entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp, "/output/entry.txt")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
