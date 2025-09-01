#!/usr/bin/env python3
import argparse, csv, json, re, sys
from pathlib import Path

VALID_TASKS = {"classify_vulns", "explain", "rewrite_fix"}

def load_labels(labels_path: Path):
    with labels_path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    issues = set(data.get("issues", []))
    severity = set(data.get("severity", []))
    return issues, severity

def split_list_field(val: str):
    """
    Split a list-like string into items.
    Supports comma, pipe, or semicolon as separators.
    """
    if val is None:
        return []
    s = val.strip()
    if not s:
        return []
    # Replace multiple separators with comma and split
    s = re.sub(r"[|;]", ",", s)
    parts = [p.strip() for p in s.split(",") if p.strip()]
    return parts

def normalize_labels(raw: str, valid_issues: set):
    items = split_list_field(raw)
    # Keep order but dedupe
    seen, out = set(), []
    for it in items:
        if it not in seen:
            seen.add(it)
            out.append(it)
    # (Optional) warn if something isn't in canonical list, but still keep it
    unknown = [x for x in out if x not in valid_issues]
    if unknown:
        sys.stderr.write(f"[warn] Unknown issue label(s): {unknown}\n")
    return out

def normalize_meta_tags(raw: str):
    return split_list_field(raw)

def row_to_obj(row, valid_issues, valid_severity):
    task = (row.get("task") or "").strip()
    if task not in VALID_TASKS:
        raise ValueError(f"Invalid or missing task: '{task}' (must be one of {sorted(VALID_TASKS)})")

    rid = (row.get("id") or "").strip()
    if not rid:
        raise ValueError("Missing 'id'")

    meta_tags = normalize_meta_tags(row.get("meta_tags", ""))

    if task == "classify_vulns":
        input_text = (row.get("input") or "").strip()
        if not input_text:
            raise ValueError(f"[{rid}] classify_vulns requires 'input'")
        labels = normalize_labels(row.get("labels", ""), valid_issues)
        if not labels:
            raise ValueError(f"[{rid}] classify_vulns requires non-empty 'labels'")
        severity = (row.get("primary_severity") or "").strip()
        if severity and severity not in valid_severity:
            sys.stderr.write(f"[warn] '{rid}' primary_severity '{severity}' not in canonical set {sorted(valid_severity)}\n")
        obj = {
            "task": task,
            "id": rid,
            "input": input_text,
            "labels": labels,
            "primary_severity": severity if severity else None,
            "meta": {"tags": meta_tags}
        }

    elif task == "explain":
        input_text = (row.get("input") or "").strip()
        response = (row.get("response") or "").strip()
        if not input_text or not response:
            raise ValueError(f"[{rid}] explain requires 'input' and 'response'")
        obj = {
            "task": task,
            "id": rid,
            "input": input_text,
            "response": response,
            "meta": {"tags": meta_tags}
        }

    elif task == "rewrite_fix":
        buggy = (row.get("buggy") or "").strip()
        fixed = (row.get("fixed") or "").strip()
        if not buggy or not fixed:
            raise ValueError(f"[{rid}] rewrite_fix requires 'buggy' and 'fixed'")
        hint = (row.get("hint") or "").strip()
        obj = {
            "task": task,
            "id": rid,
            "buggy": buggy,
            "fixed": fixed,
            "hint": hint if hint else None,
            "meta": {"tags": meta_tags}
        }

    # Drop None values for cleanliness
    obj = {k: v for k, v in obj.items() if v not in (None, [], "")}
    return obj

def main():
    ap = argparse.ArgumentParser(description="Convert seed_examples.csv to JSONL for fine-tuning.")
    ap.add_argument("--csv", required=True, help="Path to CSV (e.g., preflight_corpus/data/training/seed_examples.csv)")
    ap.add_argument("--labels", required=True, help="Path to labels.json (e.g., hf_dataset/data/meta/labels.json)")
    ap.add_argument("--out", required=True, help="Output JSONL path")
    args = ap.parse_args()

    csv_path = Path(args.csv)
    labels_path = Path(args.labels)
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    valid_issues, valid_severity = load_labels(labels_path)

    count = {"classify_vulns": 0, "explain": 0, "rewrite_fix": 0, "total": 0}
    with csv_path.open("r", encoding="utf-8", newline="") as f_in, out_path.open("w", encoding="utf-8") as f_out:
        reader = csv.DictReader(f_in)
        expected_cols = {"task","id","input","buggy","fixed","labels","primary_severity","response","hint","meta_tags"}
        missing = expected_cols - set([c.strip() for c in reader.fieldnames or []])
        if missing:
            raise ValueError(f"CSV missing expected columns: {sorted(missing)}")

        for i, row in enumerate(reader, start=2):  # start=2 accounts for header line
            try:
                obj = row_to_obj(row, valid_issues, valid_severity)
            except Exception as e:
                raise ValueError(f"Error at CSV line {i}: {e}") from e
            f_out.write(json.dumps(obj, ensure_ascii=False) + "\n")
            count["total"] += 1
            count[obj["task"]] += 1

    print(f"[ok] Wrote {count['total']} items to {out_path}")
    print(f"     classify_vulns: {count['classify_vulns']}")
    print(f"     explain       : {count['explain']}")
    print(f"     rewrite_fix   : {count['rewrite_fix']}")

if __name__ == "__main__":
    main()