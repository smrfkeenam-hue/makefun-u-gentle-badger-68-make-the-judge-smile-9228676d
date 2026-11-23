"""Make the Judge Smile — one warm line about a small good thing today.

A stranger at the market, a warm bun, and a guess that was exactly right:
warmth in the kindness, surprise in the last three words, and one concrete
detail (the bun, the market, the morning) instead of a general sentiment.

The entrypoint writes a single line (<=200 chars) to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

LINE = "This morning a stranger at the market pressed a warm bun into my hand and said, 'You look like you skipped breakfast' — she was right."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    # Gate self-check: 1-200 characters, not only whitespace, single line.
    # The check counts the line itself, without the trailing newline we write.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip(), "line must not be only whitespace"
    assert "\n" not in LINE, "line must be a single line"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"wrote {path} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
