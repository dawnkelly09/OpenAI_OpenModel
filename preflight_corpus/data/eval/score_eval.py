# score_eval.py
import csv, json
from collections import Counter, defaultdict

GOLD = "eval_key.csv"        # ground-truth answers
PREDS = "eval_preds.jsonl"   # model predictions

ALLOWED_SEV = {"Critical","High","Medium","Low","Informational"}

def split_labels(s: str):
    if not s:
        return []
    # support ; | , as separators
    for sep in [";", "|", ","]:
        if sep in s:
            parts = [p.strip() for p in s.split(sep)]
            return [p for p in parts if p]
    return [s.strip()] if s.strip() else []

def load_gold(path=GOLD):
    """Expect columns: id, labels, primary_severity (no 'task' needed)."""
    gold = {}
    with open(path, newline="") as f:
        r = csv.DictReader(f)
        required = {"id","labels","primary_severity"}
        missing = required - set(r.fieldnames or [])
        if missing:
            raise ValueError(f"Gold file missing columns: {missing}")
        for row in r:
            uid = row["id"].strip()
            labs = split_labels(row["labels"])
            sev  = row["primary_severity"].strip().capitalize()
            if sev not in ALLOWED_SEV:
                # normalize mild variations
                sev = {"info":"Informational",
                       "informational":"Informational",
                       "med":"Medium",
                       "low":"Low",
                       "high":"High",
                       "crit":"Critical"}.get(sev.lower(), "Informational")
            gold[uid] = {"labels": set(labs), "primary_severity": sev}
    return gold

def load_preds(path=PREDS):
    preds = {}
    with open(path) as f:
        for line in f:
            d = json.loads(line)
            uid = d["id"]
            pred = d.get("pred", {})
            labs = [x.strip() for x in pred.get("labels", []) if isinstance(x, str) and x.strip()]
            sev  = (pred.get("primary_severity","") or "").strip().capitalize()
            if sev not in ALLOWED_SEV:
                sev = "Informational"
            preds[uid] = {"labels": set(labs), "primary_severity": sev}
    return preds

def prf1(pred_set, gold_set):
    tp = len(pred_set & gold_set)
    fp = len(pred_set - gold_set)
    fn = len(gold_set - pred_set)
    prec = tp / (tp + fp) if (tp + fp) else 0.0
    rec  = tp / (tp + fn) if (tp + fn) else 0.0
    f1   = 2*prec*rec/(prec+rec) if (prec+rec) else 0.0
    return prec, rec, f1, tp, fp, fn

def main():
    gold = load_gold()
    preds = load_preds()

    # --- Per-item macro metrics (multi-label) ---
    per_item = []
    sev_correct = 0
    sev_confusion = Counter()
    empty_pred = 0

    # Per-label counters
    label_tp = Counter()
    label_fp = Counter()
    label_fn = Counter()

    all_labels = set()

    for uid, g in gold.items():
        p = preds.get(uid, {"labels": set(), "primary_severity":"Informational"})
        pset, gset = p["labels"], g["labels"]
        all_labels |= gset | pset

        prec, rec, f1, tp, fp, fn = prf1(pset, gset)
        per_item.append((prec, rec, f1))

        if not pset:
            empty_pred += 1

        # accumulate per-label counts
        for lab in (pset & gset):
            label_tp[lab] += 1
        for lab in (pset - gset):
            label_fp[lab] += 1
        for lab in (gset - pset):
            label_fn[lab] += 1

        # severity
        sev_pred = p["primary_severity"]
        sev_gold = g["primary_severity"]
        if sev_pred == sev_gold:
            sev_correct += 1
        else:
            sev_confusion[(sev_gold, sev_pred)] += 1

    n = len(gold) or 1
    macro_prec = sum(x[0] for x in per_item) / n
    macro_rec  = sum(x[1] for x in per_item) / n
    macro_f1   = sum(x[2] for x in per_item) / n
    sev_acc    = sev_correct / n

    print("=== Baseline Scoring ===")
    print(f"Items evaluated: {n}")
    print(f"Labels (macro over items) → Precision: {macro_prec:.2f}  Recall: {macro_rec:.2f}  F1: {macro_f1:.2f}")
    print(f"Severity accuracy: {sev_acc:.2f}")
    print(f"Empty label predictions: {empty_pred}/{n} ({empty_pred/n:.2%})")
    print()

    # --- Per-label report ---
    print("=== Per-label Precision/Recall/F1 (support ≥ 1 in gold) ===")
    rows = []
    for lab in sorted(all_labels):
        tp, fp, fn = label_tp[lab], label_fp[lab], label_fn[lab]
        support = tp + fn
        if support == 0:
            continue
        prec = tp / (tp + fp) if (tp + fp) else 0.0
        rec  = tp / (tp + fn) if (tp + fn) else 0.0
        f1   = 2*prec*rec/(prec+rec) if (prec+rec) else 0.0
        rows.append((lab, support, tp, fp, fn, prec, rec, f1))
    # sort by support desc, then F1 desc
    rows.sort(key=lambda x: (-x[1], -x[7]))
    print(f"{'Label':38}  {'Sup':>3}  {'TP':>3}  {'FP':>3}  {'FN':>3}   {'P':>5}  {'R':>5}  {'F1':>5}")
    for lab, sup, tp, fp, fn, p, r, f1 in rows[:25]:
        print(f"{lab:38}  {sup:>3}  {tp:>3}  {fp:>3}  {fn:>3}   {p:5.2f}  {r:5.2f}  {f1:5.2f}")

    # --- Severity confusion (top 10) ---
    if sev_confusion:
        print("\n=== Severity Confusions (Gold → Pred) ===")
        for (gsev, psev), c in sev_confusion.most_common(10):
            print(f"{gsev:14} → {psev:14} : {c}")

if __name__ == "__main__":
    main()
