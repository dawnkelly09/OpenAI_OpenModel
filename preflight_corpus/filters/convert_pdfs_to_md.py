from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
from pathlib import Path
from typing import List, Tuple, Optional

# --------------------------- CLI Utilities ---------------------------

def have_cli(cmd: str) -> bool:
    return shutil.which(cmd) is not None

def run(cmd: List[str], input_text: Optional[str] = None, timeout: int = 300) -> Tuple[int, str, str]:
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    out, err = proc.communicate(input=input_text, timeout=timeout)
    return proc.returncode, out, err

# --------------------------- Cleaning Heuristics ---------------------------

def normalize_whitespace(text: str) -> str:
    # Strip trailing spaces
    text = re.sub(r'[ \t]+$', '', text, flags=re.MULTILINE)
    # Collapse 3+ blank lines to max 2
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip() + '\n'

def remove_common_header_footer(pages: List[str]) -> List[str]:
    """
    Try to remove per-page repeated header/footer lines.
    We take first 2 and last 2 lines of each page, find lines that repeat on many pages, remove them.
    """
    from collections import Counter

    def head_foot_candidates(lines: List[str]) -> List[str]:
        lines = [l.rstrip() for l in lines if l.strip() != '']
        if not lines:
            return []
        top = lines[:2]
        bottom = lines[-2:] if len(lines) >= 2 else lines[-1:]
        return [*top, *bottom]

    c = Counter()
    page_lines = []
    for p in pages:
        ls = p.splitlines()
        page_lines.append(ls)
        for cand in head_foot_candidates(ls):
            c[cand] += 1

    # Consider a line as header/footer if it appears on >= 30% of pages and not too short
    threshold = max(2, int(0.3 * max(1, len(pages))))
    repeated = {line for line, cnt in c.items() if cnt >= threshold and len(line) >= 4}

    cleaned_pages = []
    for ls in page_lines:
        cleaned = []
        for line in ls:
            if line.rstrip() in repeated:
                continue
            cleaned.append(line)
        cleaned_pages.append('\n'.join(cleaned))
    return cleaned_pages

def fix_wrapped_lines(text: str) -> str:
    """
    Merge lines that look like they belong to the same paragraph.
    Heuristic: if a line does not end with sentence-final punctuation and next line is lowercase-starting, join.
    """
    lines = text.splitlines()
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        # End of paragraph markers
        if i + 1 < len(lines):
            next_line = lines[i + 1]
            # If current is not blank, next is not blank, and looks like a soft wrap -> join
            if line.strip() and next_line.strip():
                end_punct = re.search(r'[.!?:)\]]$|`$', line.strip())
                next_starts_lower = re.match(r'^[a-z0-9]', next_line.strip()) is not None
                # Avoid joining if current line ends with two spaces (explicit Markdown line break)
                if not end_punct and next_starts_lower and not line.endswith('  '):
                    line = line.rstrip() + ' ' + next_line.lstrip()
                    i += 1
                    # Keep joining while the heuristic holds
                    while i + 1 < len(lines):
                        nl = lines[i + 1]
                        if nl.strip():
                            end_punct = re.search(r'[.!?:)\]]$|`$', line.strip())
                            next_starts_lower = re.match(r'^[a-z0-9]', nl.strip()) is not None
                            if not end_punct and next_starts_lower and not line.endswith('  '):
                                line = line.rstrip() + ' ' + nl.lstrip()
                                i += 1
                                continue
                        break
        out.append(line)
        i += 1
    return '\n'.join(out)

# --------------------------- Extractors ---------------------------

def extract_with_pandoc(pdf_path: Path) -> Optional[str]:
    if not have_cli("pandoc"):
        return None
    # pandoc can read PDFs via embedded PDF readers on some platforms, but often needs pdftotext.
    # We'll try: pandoc input.pdf -t gfm
    code, out, err = run(["pandoc", str(pdf_path), "-t", "gfm", "--wrap=none"])
    if code == 0 and out.strip():
        return out
    return None

def extract_with_pymupdf(pdf_path: Path) -> Optional[str]:
    try:
        import fitz  # PyMuPDF
    except Exception:
        return None
    try:
        doc = fitz.open(pdf_path)
        pages = []
        for page in doc:
            # Use textpage extraction with "blocks" to preserve some structure
            txt = page.get_text("text")
            pages.append(txt)
        doc.close()
        pages = remove_common_header_footer(pages)
        text = "\n\n".join(pages)
        return text
    except Exception:
        return None

def extract_with_pdfminer(pdf_path: Path) -> Optional[str]:
    try:
        from pdfminer.high_level import extract_text
    except Exception:
        return None
    try:
        text = extract_text(str(pdf_path))
        return text
    except Exception:
        return None

def extract_with_pdftotext(pdf_path: Path) -> Optional[str]:
    if not have_cli("pdftotext"):
        return None
    code, out, err = run(["pdftotext", "-layout", str(pdf_path), "-"])
    if code == 0 and out.strip():
        return out
    return None

# --------------------------- Main Conversion ---------------------------

def convert_pdf(pdf_path: Path, out_dir: Path, fmt: str = "md") -> Tuple[bool, str]:
    """
    Returns (success, message). Writes output file to out_dir with .md or .txt extension.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / (pdf_path.stem + (".md" if fmt == "md" else ".txt"))

    text = None
    used = None

    # 1) Try pandoc (Markdown)
    if fmt == "md":
        text = extract_with_pandoc(pdf_path)
        if text:
            used = "pandoc"

    # 2) Try PyMuPDF (text)
    if text is None:
        text = extract_with_pymupdf(pdf_path)
        if text:
            used = "pymupdf"

    # 3) Try pdfminer (text)
    if text is None:
        text = extract_with_pdfminer(pdf_path)
        if text:
            used = "pdfminer"

    # 4) Try pdftotext (text)
    if text is None:
        text = extract_with_pdftotext(pdf_path)
        if text:
            used = "pdftotext"

    if text is None:
        return False, f"Failed to extract: {pdf_path.name}"

    # Cleaning / normalization
    text = fix_wrapped_lines(text)
    text = normalize_whitespace(text)

    # If we promised markdown but only got plain text, lightly wrap as Markdown
    if fmt == "md" and used in {"pymupdf", "pdfminer", "pdftotext"}:
        # Add a title if likely present in first line
        first_line = text.splitlines()[0] if text else ""
        if first_line and not first_line.startswith("#"):
            text = f"# {first_line}\n\n" + "\n".join(text.splitlines()[1:])
    try:
        out_path.write_text(text, encoding="utf-8")
    except Exception as e:
        return False, f"Write error for {pdf_path.name}: {e}"

    return True, f"{pdf_path.name} -> {out_path.name} via {used}"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", "-i", required=True, help="Input folder containing PDFs")
    ap.add_argument("--output", "-o", required=True, help="Output folder for MD/TXT")
    ap.add_argument("--format", "-f", default="md", choices=["md", "txt"], help="Output format")
    args = ap.parse_args()

    in_dir = Path(args.input)
    out_dir = Path(args.output)

    if not in_dir.exists():
        print(f"Input dir not found: {in_dir}")
        return

    pdfs = sorted(in_dir.rglob("*.pdf"))
    if not pdfs:
        print(f"No PDFs found under {in_dir}")
        return

    successes, failures = [], []
    for pdf in pdfs:
        ok, msg = convert_pdf(pdf, out_dir, fmt=args.format)
        (successes if ok else failures).append(msg)
        print(msg)

    print("\n--- Summary ---")
    print(f"Converted: {len(successes)}")
    print(f"Failed:    {len(failures)}")
    if failures:
        print("Failures:")
        for m in failures:
            print("  -", m)

if __name__ == "__main__":
    main()