"""Convert datasheet PDFs to Markdown so they can be searched cheaply.

Each PDF gets a .md file next to it. PDFs whose .md is already newer are skipped.

Usage:
    python tools/pdf2md.py              # converts PDFs under hardware/datasheets/
    python tools/pdf2md.py some/folder  # converts PDFs under another folder
    python tools/pdf2md.py file.pdf     # converts a single PDF

Requires: pip install pymupdf4llm   (PyMuPDF is AGPL-3.0)
"""
import sys
from pathlib import Path

import pymupdf4llm


def needs_update(pdf: Path, md: Path) -> bool:
    """True if the .md is missing or older than the PDF."""
    if not md.exists():
        return True
    return md.stat().st_mtime < pdf.stat().st_mtime


def convert(pdf: Path, md: Path) -> None:
    """Convert one PDF to Markdown, writing the result as UTF-8."""
    text = pymupdf4llm.to_markdown(str(pdf))
    md.write_text(text, encoding="utf-8")


def find_pdfs(target: Path) -> list[Path]:
    """A single PDF, or every PDF under a folder (subfolders included).

    The suffix is compared in lowercase so "X.PDF" is found as well as "x.pdf"
    (glob("*.pdf") is case-sensitive on Linux).
    """
    if target.is_file():
        return [target]
    return sorted(p for p in target.rglob("*") if p.is_file() and p.suffix.lower() == ".pdf")


def main() -> int:
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("hardware/datasheets")
    if not target.exists():
        print(f"Not found: {target}")
        return 2

    converted, skipped, failed = 0, 0, []

    for pdf in find_pdfs(target):
        md = pdf.with_suffix(".md")
        if not needs_update(pdf, md):
            skipped += 1
            continue
        print(f"Converting {pdf} ...", flush=True)
        try:
            convert(pdf, md)
            converted += 1
        except Exception as exc:  # one bad PDF should not stop the rest
            print(f"  FAILED: {exc}")
            failed.append(pdf)

    print(f"\nDone: {converted} converted, {skipped} up to date, {len(failed)} failed")
    for pdf in failed:
        print(f"  failed: {pdf}")

    # Non-zero exit code on failure, so the script can be chained (&&) or used in CI
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
