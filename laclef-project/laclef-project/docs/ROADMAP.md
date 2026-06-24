# Roadmap

Where La Clef is headed. Roughly in order, but not set in stone.

## Near term — polish the current French app

- **Make the fighter's top forms more distinct.** Right now the last three transformations (Super Saiyan 2 / 3 / Ultra) look fairly similar to each other. Plan: push the high-end forms further apart — a hair-color shift toward white/blue at the very top, a ground-glow or energy ring, maybe a more dramatic pose — so hitting the final form feels like a real payoff.
- **Keep tightening the text.** A handful of the book's two-column vocabulary tables were merged by the scan in ways that can't be perfectly rebuilt; a few glosses still carry a stray trailing word. These are cosmetic and get fixed as they're spotted.
- **A free tutor by default.** Wire the app to a local model (Ollama) out of the box so the tutor works for everyone with no API key, fully offline.

## Medium term — make it easy to host and share

- A simple hosted version so anyone can try it from a link (with progress that saves across sessions).
- A short "first time here?" walkthrough.
- Optional: package it so it installs like an app on a phone.

## The big one — Madrigal's Magic Key to **Spanish**

Same engine, different book. Madrigal wrote a Spanish companion to the French primer, built on the exact same cognate-bridge method. The plan is to reuse everything here — the reader, the exercises, the voice, the themes, and the fighter — and feed it the Spanish lessons.

What carries over directly:
- the whole app shell and design
- the exercise hide/reveal and sentence-builder chips
- the leveling and the fighter (he'd just speak Spanish — "Aprendiz" instead of "Apprenti," and so on)
- the OCR → clean → structure pipeline

What's new for the Spanish edition:
- OCR and clean the Spanish source text
- adjust the French-vs-English language detection to Spanish-vs-English
- Spanish voice (the browser already supports `es-ES` / `es-MX`)
- Spanish rank names for the fighter's forms

After Spanish, the same approach could extend to the other books in the series.

## Maybe someday

- Spaced-repetition review built from the vocabulary you've seen.
- A streak calendar and longer-term stats.
- Picking a different companion character or art style.
