# preflight_corpus/data/training/render_sft_flex.py
import os, json, hashlib, sys
from typing import List, Dict, Any, Iterable

# --------- Config ----------
SEED_PATH = "preflight_corpus/data/training/seed_examples.jsonl"  # accepts .json or .jsonl
OUT_DIR   = "hf_dataset/data/sft"  # will write train/val/test.jsonl here
SPLITS    = ("train", "val", "test")
RATIOS    = (0.80, 0.10, 0.10)     # used only if we must split the single seed
ALLOWED_SEV = {"Critical","High","Medium","Low","Informational"}

SYS = (
  "You are PreFlight. Follow the task exactly. "
  "For classify_vulns: return ONLY one JSON object with keys "
  '"labels" (array of strings) and "primary_severity" (one of '
  '[Critical, High, Medium, Low, Informational]). No extra text.'
)

# --------- IO helpers ----------
def read_json_or_jsonl(path: str) -> List[Dict[str, Any]]:
    if not os.path.exists(path):
        return []
    items = []
    with open(path, "r", encoding="utf-8") as f:
        text = f.read().strip()
        if not text:
            return []
        # Try JSON array first
        try:
            parsed = json.loads(text)
            if isinstance(parsed, list):
                return parsed
        except Exception:
            pass
    # Fallback: newline-delimited JSON
    with open(path, "r", encoding="utf-8") as f:
        for ln in f:
            ln = ln.strip()
            if not ln:
                continue
            items.append(json.loads(ln))
    return items

def write_jsonl(path: str, rows: Iterable[Dict[str, Any]]):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

# --------- Build prompt/response ----------
def build_prompt(item: Dict[str, Any]) -> str:
    t = (item.get("task") or "").strip()
    parts = [f"[SYSTEM]\n{SYS}\n"]
    if t == "classify_vulns":
        parts.append("[TASK] classify_vulns")
        parts.append("[SNIPPET]\n" + (item.get("input") or ""))
    elif t == "explain":
        parts.append("[TASK] explain")
        parts.append("[SNIPPET]\n" + (item.get("input") or ""))
    elif t == "rewrite_fix":
        parts.append("[TASK] rewrite_fix")
        src = item.get("buggy") or item.get("input") or ""
        parts.append("[SNIPPET]\n" + src)
    else:
        parts.append("[TASK] unknown")
    return "\n".join(parts).strip()

def norm_severity(s: str) -> str:
    if not s:
        return "Informational"
    s = s.strip().capitalize()
    # Capitalize maps "critical"->"Critical", etc.; allow "Informational" passthrough
    if s.lower() == "informational":
        s = "Informational"
    return s if s in ALLOWED_SEV else "Informational"

def build_response(item: Dict[str, Any]) -> str:
    t = (item.get("task") or "").strip()
    if t == "classify_vulns":
        labels = [x for x in (item.get("labels") or []) if isinstance(x, str) and x.strip()]
        if not labels:
            return ""
        sev = norm_severity(item.get("primary_severity") or "")
        return json.dumps({"labels": labels, "primary_severity": sev})
    elif t == "explain":
        return (item.get("response") or "").strip()
    elif t == "rewrite_fix":
        return (item.get("fixed") or "").strip()
    return ""

# --------- Split strategy (stable by id hash) ----------
def stable_bucket(example_id: str) -> str:
    # Map id -> [0,1); split by cumulative ratios
    h = hashlib.sha256(example_id.encode("utf-8")).digest()
    val = int.from_bytes(h[:8], "big") / 2**64
    b0 = RATIOS[0]
    b1 = RATIOS[0] + RATIOS[1]
    if val < b0: return "train"
    if val < b1: return "val"
    return "test"

# --------- Pipeline ----------
def render_items(items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    out = []
    dropped = 0
    per_task = {"classify_vulns": 0, "explain": 0, "rewrite_fix": 0}
    for ex in items:
        resp = build_response(ex)
        if not resp:
            dropped += 1
            continue
        row = {
            "prompt": build_prompt(ex),
            "response": resp,
            "task": ex.get("task"),
            "id": ex.get("id")
        }
        out.append(row)
        if row["task"] in per_task:
            per_task[row["task"]] += 1
    return out, dropped, per_task

def load_existing_splits() -> Dict[str, List[Dict[str, Any]]]:
    splits = {}
    found = False
    for sp in SPLITS:
        p = os.path.join(OUT_DIR, f"{sp}.jsonl")
        if os.path.exists(p):
            splits[sp] = read_json_or_jsonl(p)
            found = True
        else:
            splits[sp] = []
    return splits if found else {}

def main():
    existing = load_existing_splits()
    if existing:
        # Re-render in-place (keeps the same split membership)
        print("[info] Found existing splits; re-rendering them in place.")
        for sp in SPLITS:
            src_path = os.path.join(OUT_DIR, f"{sp}.jsonl")
            raw = read_json_or_jsonl(src_path)
            # raw here is already prompt/response? If so, we should re-derive from seed instead.
            # Safer: regenerate from seed if available, using ids in this split.
        # Load full seed and filter by ids present in each split
        seed = read_json_or_jsonl(SEED_PATH)
        by_id = {ex.get("id"): ex for ex in seed if ex.get("id")}
        for sp in SPLITS:
            split_ids = []
            # try to load an id list file if present; otherwise infer from prior rows
            prev_rows = read_json_or_jsonl(os.path.join(OUT_DIR, f"{sp}.jsonl"))
            for r in prev_rows:
                rid = r.get("id")
                if rid: split_ids.append(rid)
            # rebuild from seed by those ids
            subset = [by_id[i] for i in split_ids if i in by_id]
            rows, dropped, per_task = render_items(subset)
            write_jsonl(os.path.join(OUT_DIR, f"{sp}.jsonl"), rows)
            print(f"[ok] {sp}.jsonl → kept={len(rows)}, dropped={dropped}, per_task={per_task}")
        return

    # No existing splits → read seed and split deterministically
    seed = read_json_or_jsonl(SEED_PATH)
    if not seed:
        print(f"[error] No data found. Checked: {SEED_PATH} and {OUT_DIR}/train|val|test.jsonl")
        sys.exit(1)

    # Group by hash bucket (stable)
    buckets = {"train": [], "val": [], "test": []}
    for ex in seed:
        ex_id = ex.get("id") or json.dumps(ex, sort_keys=True)
        buckets[stable_bucket(ex_id)].append(ex)

    # Render and write
    for sp in SPLITS:
        rows, dropped, per_task = render_items(buckets[sp])
        write_jsonl(os.path.join(OUT_DIR, f"{sp}.jsonl"), rows)
        print(f"[ok] {sp}.jsonl → kept={len(rows)}, dropped={dropped}, per_task={per_task}")

    # Global summary
    total_kept = sum(len(read_json_or_jsonl(os.path.join(OUT_DIR, f"{sp}.jsonl"))) for sp in SPLITS)
    print(f"[summary] total_kept={total_kept}  out_dir={OUT_DIR}")

if __name__ == "__main__":
    main()
