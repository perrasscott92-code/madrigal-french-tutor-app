#!/usr/bin/env python3
"""
process_lessons.py
==================

Turns the raw OCR text of the 1959 book into the clean, structured
lesson data the app uses.

This is a reference/documentation version of the pipeline that was used to
build data/lessons.json. It shows the steps; you don't need to re-run it
unless you re-OCR the source.

PIPELINE OVERVIEW
-----------------
1.  OCR the scanned PDF page images with Tesseract (French + English packs):
        pdftoppm -png -r 150 book.pdf page
        tesseract page-NN.png out -l fra+eng --psm 4
    The French language pack is essential — without it every accent is lost.

2.  Segment the full text into 48 lessons + the preface. The book labels
    lessons as "LESSON NUMBER ONE" ... "LESSON NUMBER FORTY-EIGHT".
    Watch out for two traps:
      - the table of contents repeats those labels (skip it),
      - "THIRTY" matches inside "THIRTY-SEVEN" (use word-boundary matching).

3.  Clean each lesson:
      - strip page markers, running headers, and bare page-number lines
      - repair hyphenation that the scan split across line breaks
        ("mate-\nrial" -> "material")
      - fix recurring OCR misreads ("Nore:" -> "Note:", "musculine" ->
        "masculine", "Theretore" -> "Therefore", etc.)
      - reflow the preface prose into real paragraphs

4.  Save as JSON keyed "0" (preface) .. "48".

The display-time formatting (coloring French vs English, splitting the
OCR-merged two-column tables, the exercise hide/reveal, the word-bank chips)
is all done in the browser by the app — see app/la-clef.html.
"""

import json
import re
import sys


def strip_junk_lines(text: str) -> str:
    """Remove page markers, running headers, and bare page-number lines."""
    out = []
    for line in text.split("\n"):
        t = line.strip()
        if re.match(r"^\s*=====\s*PAGE", line):
            continue
        if re.match(r"^[‘'\"\s]*LE[ÇCG]ON\s+NUM[ÉE]RO\b", t, re.I):
            continue
        if re.match(r"^\s*(?:[ivxlc]{1,4}\s+)?PREFACE\s*$", t, re.I):
            continue
        if re.match(r"^\s*\d{1,3}\s*$", t):  # a lone page number
            continue
        out.append(line)
    return "\n".join(out)


def repair_hyphenation(text: str) -> str:
    """Rejoin words the scan split across a line break: 'mate-\\nrial' -> 'material'."""
    text = re.sub(r"([A-Za-zÀ-ÿ])-\n\n+([a-zà-ÿ])", r"\1\2", text)
    text = re.sub(r"([A-Za-zÀ-ÿ])-\n([a-zà-ÿ])", r"\1\2", text)
    return text


def common_fixes(text: str) -> str:
    """Fix recurring OCR misreads observed across the whole book."""
    fixes = {
        r"\bNore:": "Note:",
        r"\bmusculine\b": "masculine",
        r"\bTheretore\b": "Therefore",
        r"\bmatetial\b": "material",
        r"\bilest\b": "il est",
        r"\bétre\b": "être",
    }
    for pat, repl in fixes.items():
        text = re.sub(pat, repl, text)
    text = re.sub(r" {2,}", " ", text)
    return text


def clean_lesson(text: str) -> str:
    text = strip_junk_lines(text)
    text = repair_hyphenation(text)
    text = common_fixes(text)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    return text


def main():
    if len(sys.argv) < 3:
        print("usage: python process_lessons.py raw_lessons.json out_lessons.json")
        print("(raw_lessons.json = segmented-but-uncleaned lessons keyed '0'..'48')")
        sys.exit(1)

    raw = json.load(open(sys.argv[1], encoding="utf-8"))
    cleaned = {k: clean_lesson(v) for k, v in raw.items()}
    json.dump(
        cleaned,
        open(sys.argv[2], "w", encoding="utf-8"),
        ensure_ascii=False,
        separators=(",", ":"),
    )
    print(f"Wrote {len(cleaned)} sections to {sys.argv[2]}")


if __name__ == "__main__":
    main()
