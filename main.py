"""One Line, One Laugh — make.fun entry.

Writes a single funny line (at most 200 characters) to /output/entry.txt.

The line: a customer asks the barista for "something strong" expecting a
strong coffee; the barista hands over her resignation letter instead —
the strongest thing in the shop.
"""

import os

ENTRY = "I asked the barista for something strong. She handed me her resignation letter."


def output_path():
    """Return the path the entry text is written to."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def main():
    """Write the entry line to /output/entry.txt and report its length."""
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
