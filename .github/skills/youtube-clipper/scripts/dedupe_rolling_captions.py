#!/usr/bin/env python3
"""
Dedupe rolling-caption repetitions in a transcript.

YouTube auto-generated VTTs often use a sliding window where each new caption
frame repeats part of the previous frame. When you flatten such a VTT to plain
text, you get sequences like:

    I left everything I knew in Toronto and I left everything I knew in Toronto
    and moved to Hong Kong to start over. This moved to Hong Kong to start
    over. This moved to Hong Kong to start over. This is a story...

`vtt_to_shadow_srt.py` handles most VTT variants, but not this particular
rolling pattern. This script cleans it up after-the-fact by scanning for
adjacent n-gram repeats (n from 30 down to 2) and collapsing them.

Usage:
    python3 dedupe_rolling_captions.py <input.txt> [output.txt]
    python3 dedupe_rolling_captions.py -            # stdin -> stdout
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


def dedupe_ngrams(words: list[str], max_n: int = 30) -> list[str]:
    """Collapse adjacent identical n-grams.

    Loops until no more collapses happen. Tries longer n first so that a
    6-word repeat is collapsed as one unit instead of as three 2-word repeats
    (which would over-delete).
    """
    changed = True
    while changed:
        changed = False
        for n in range(max_n, 1, -1):
            out: list[str] = []
            i = 0
            while i < len(words):
                end1 = i + n
                end2 = i + 2 * n
                if end2 <= len(words) and words[i:end1] == words[end1:end2]:
                    out.extend(words[i:end1])
                    i = end2
                    changed = True
                    # keep collapsing if the same phrase repeats further
                    while i + n <= len(words) and words[i - n:i] == words[i:i + n]:
                        i += n
                else:
                    out.append(words[i])
                    i += 1
            words = out
    return words


def clean(text: str) -> str:
    words = text.split()
    deduped = dedupe_ngrams(words)
    return re.sub(r"\s+", " ", " ".join(deduped)).strip()


def main(argv: list[str]) -> int:
    if len(argv) < 2 or argv[1] in ("-h", "--help"):
        print(__doc__)
        return 0

    src = argv[1]
    text = sys.stdin.read() if src == "-" else Path(src).read_text(encoding="utf-8")

    before = len(text.split())
    cleaned = clean(text)
    after = len(cleaned.split())

    if len(argv) >= 3:
        Path(argv[2]).write_text(cleaned, encoding="utf-8")
        print(f"Before: {before} words  After: {after} words", file=sys.stderr)
    else:
        sys.stdout.write(cleaned)

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
