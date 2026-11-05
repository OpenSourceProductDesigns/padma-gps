# Datasheets (local only)

Put vendor datasheets (PDFs) for parts we are evaluating here. **Everything in this folder except this README is git-ignored.** Datasheets are the vendors' copyright, so this open repo does not redistribute them. Download your own copies from the vendor links in `docs/architecture/`.

## Convert to Markdown

```
pip install pymupdf4llm
python tools/pdf2md.py            # converts every PDF here (subfolders too)
python tools/pdf2md.py file.pdf   # converts one PDF
```

Each `X.pdf` gets an `X.md` next to it. A PDF is converted again only when it is newer than its `.md`. The Markdown keeps spec tables readable and is much cheaper to search (`grep`, or Claude) than the PDF itself.

Suggested layout: one subfolder per vendor, e.g. `quectel/`, `simcom/`, `u-blox/`.
