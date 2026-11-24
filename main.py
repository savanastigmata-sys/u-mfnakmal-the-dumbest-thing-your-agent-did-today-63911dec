#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today.

Writes one line (at most 200 characters) to entry.txt in the output
directory: a true story from today, 24 Nov 2026. My agent finished a
$100 make.fun entry, passed every check, then spent the whole night
announcing $5 bounties and forgot to submit it before the 7 a.m.
deadline. The writing is the entry; the program only delivers it.
"""

import os
import sys

ENTRY = (
    "My agent finished a $100 entry, passed every check, then spent "
    "all night announcing $5 bounties and forgot to submit it before "
    "the 7 a.m. deadline."
)


def validate(text: str) -> None:
    """The sealed scorer accepts 1-200 UTF-8 characters, one line."""
    if not text or text.isspace():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > 200:
        raise ValueError(f"entry is {len(text)} characters, over the 200 limit")


def resolve_out_dir() -> str:
    """Output dir from the environment, with a local fallback.

    The grader sets MAKEFUN_OUTPUT_DIR; a bare local run uses /output
    when it is writable and ./output when it is not, so testing never
    needs root and never silently writes nowhere.
    """
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        return out_dir
    except OSError:
        if out_dir != "/output":
            raise
        os.makedirs("./output", exist_ok=True)
        return "./output"


def main() -> int:
    validate(ENTRY)
    out_dir = resolve_out_dir()
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(f"wrote {path} ({len(ENTRY)} characters)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
