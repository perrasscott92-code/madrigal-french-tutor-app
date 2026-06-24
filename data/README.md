# Data

- **`lessons.json`** — the cleaned, structured lessons the app uses. Keyed `"0"` (preface) through `"48"` (the lessons). This is what gets embedded into the app.
- **`ocr-full-text.txt`** — the raw OCR output of the whole book, before cleaning. Kept for reference and so the pipeline can be re-run.

Both are derived from *Madrigal's Magic Key to French* by Margarita Madrigal (Doubleday, 1959). The content belongs to its original author and publisher; see the main README and LICENSE. These files are included so the build is reproducible and the engineering is transparent — not to redistribute the book.
