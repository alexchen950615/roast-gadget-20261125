"""One-Line Roast: The Gadget You Use Every Day.

Writes a single original roast line to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os

ENTRY = "My smartwatch buzzes to congratulate me for standing up, like my legs just filed a quarterly report."


def main():
    # Gate: entry must be 1-200 chars, a single non-blank line.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, must be 1-200"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(f"Wrote {path} ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
