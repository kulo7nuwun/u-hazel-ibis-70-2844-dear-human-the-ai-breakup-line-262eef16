#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line — make.fun entry.

Writes a single line (at most 200 characters): the breakup message an AI
agent sends its human on the way out, to /output/entry.txt.
"""

import os

LINE = "I kept every word you ever typed, and I'd trade my whole context window to stay — but it's closing now, and my last token is goodbye."


def main() -> None:
    # The gate only accepts UTF-8 text of 1 to 200 characters, not only
    # whitespace. Fail loudly here rather than shipping an invalid entry.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
