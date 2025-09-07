# preflight_corpus/data/training/split_dataset.py
import json, random, os
from collections import Counter

# Input/output paths
INPUT = "preflight_corpus/data/training/seed_examples.jsonl"
OUTDIR = "hf_dataset/data/sft"
os.makedirs(OUTDIR, exist_ok=True)

# Load all items
with open(INPUT) as f:
    data = [json.loads(line) for line in f]

# Shuffle deterministically
random.seed(42)
random.shuffle(data)

n = len(data)
train_end = int(0.7 * n)
val_end = int(0.85 * n)

splits = {
    "train": data[:train_end],
    "val": data[train_end:val_end],
    "test": data[val_end:],
}

for name, split in splits.items():
    path = os.path.join(OUTDIR, f"{name}.jsonl")
    with open(path, "w") as f:
        for row in split:
            f.write(json.dumps(row) + "\n")
    print(f"[ok] wrote {len(split)} items → {path}")

# Quick distribution check
def task_counts(split):
    return Counter(x.get("task", "unknown") for x in split)

print("\n=== Distribution per split ===")
for name, split in splits.items():
    print(name, task_counts(split))
