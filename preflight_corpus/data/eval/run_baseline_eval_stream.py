import csv, json, requests, time, sys, re, os

MODEL = "gpt-oss:20b"
SYS = open("system_security.txt","r").read()

ALLOWED = {
    "Reentrancy","Access Control","Authorization Bypass","ERC Conformance",
    "Integer Overflow/Underflow","Unchecked Call","Delegatecall Misuse",
    "Oracle Manipulation","Timestamp Dependence","tx.origin Misuse",
    "Insecure Randomness","DoS via Unbounded Loop","DoS via Unexpected Revert",
    "Front-Running / MEV","Arithmetic/Overflow","Storage Collision",
    "Signature Replay","Signature Malleability","Permit/Signature Misuse",
    "Fee-On-Transfer Token Misaccounting","Slippage Misuse","Broken Invariant",
    "Gas Griefing","Precision / Reward Accounting","Proxy/Clones|Deployment",
    "Upgradeability|ERC Conformance","Allowance Race","Bypass Pause / Circuit Breaker"
}
SEV = {"Critical","High","Medium","Low","Informational"}

LABEL_MAP = {
    "UncheckedCallResult":"Unchecked Call",
    "Unchecked Call Result":"Unchecked Call",
    "Unchecked low-level call":"Unchecked Call",
    "Unchecked Low-Level Call":"Unchecked Call",
    "AccessControl":"Access Control",
    "AuthorizationBypass":"Authorization Bypass",
    "Oracle":"Oracle Manipulation",
    "Randomness":"Insecure Randomness",
    "TxOrigin":"tx.origin Misuse",
    "DoS Loop":"DoS via Unbounded Loop",
    "Arithmetic":"Arithmetic/Overflow",
}

def fewshot():
    return (
        "Example\n"
        "SNIPPET:\n(bool ok, ) = target.call(data); // ignores ok\n"
        "OUTPUT:\n"
        '{"labels":["Unchecked Call"], "primary_severity":"Medium"}\n\n'
    )

def make_prompt(uid, snippet):
    return (
        fewshot() +
        f"ID: {uid}\nTASK: classify_vulns\nSNIPPET:\n{snippet}\n\n"
        "Return ONLY the JSON object:\n"
        '{"labels":[...], "primary_severity":"..."}'
    )

def stream_once(payload, timeout=900):
    # Stream to avoid read timeouts
    with requests.post("http://localhost:11434/api/generate",
                       json=payload, timeout=timeout, stream=True) as r:
        r.raise_for_status()
        parts = []
        for line in r.iter_lines(decode_unicode=True):
            if not line: 
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue
            if "response" in obj:
                parts.append(obj["response"])
            if obj.get("done"):
                break
        return "".join(parts)

def ask(prompt, num_predict=384, retries=3):
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "system": SYS,
        "options": {
            "temperature": 0.2,
            "top_p": 0.9,
            "num_predict": num_predict,
            # keep the model warm in RAM between calls
            "num_ctx": 2048
        },
        "keep_alive": "1h",
        "stream": True
    }
    for i in range(retries):
        try:
            return stream_once(payload, timeout=900)
        except (requests.ReadTimeout, requests.ConnectionError) as e:
            if i == retries-1:
                raise
            wait = 5*(i+1)
            print(f"[warn] stream timeout, retry in {wait}s ({e})", file=sys.stderr)
            time.sleep(wait)

def coerce_json(s: str):
    s = s.strip()
    # JSON-in-a-string
    if s.startswith('"') and s.endswith('"'):
        try:
            s = json.loads(s)
        except Exception:
            pass
    # direct
    try:
        return json.loads(s)
    except Exception:
        a, b = s.find("{"), s.rfind("}")
        if a != -1 and b != -1 and b > a:
            return json.loads(s[a:b+1])
        # two-line fallback: labels: [...] / primary_severity: X
        m = re.search(r"labels:\s*\[([^\]]*)\]", s, re.I)
        labs = []
        if m:
            labs = [x.strip() for x in m.group(1).split(",") if x.strip()]
        m2 = re.search(r"primary_severity:\s*([A-Za-z]+)", s, re.I)
        sev = m2.group(1).strip().capitalize() if m2 else "Informational"
        return {"labels": labs, "primary_severity": sev}

def normalize(d):
    labs = []
    for lab in d.get("labels", []):
        if not isinstance(lab, str): 
            continue
        lab = LABEL_MAP.get(lab, lab).replace("_"," ").strip()
        if lab in ALLOWED and lab not in labs:
            labs.append(lab)
    sev = d.get("primary_severity","").strip().capitalize()
    if sev not in SEV:
        sev = "Informational"
    return {"labels": labs, "primary_severity": sev}

def continue_if_incomplete(raw, ctx_prompt):
    # If we didn’t capture {...}, ask to continue with same prompt (keeps KV cache)
    if "{" in raw and "}" in raw:
        return raw
    tail = ask(ctx_prompt + "\n\nContinue. Output ONLY the JSON now.", num_predict=256, retries=2)
    return (raw + tail).strip()

def main():
    os.makedirs("eval_debug", exist_ok=True)
    rows, fails = [], 0

    with open("eval_items.csv", newline="") as f:
        for row in csv.DictReader(f):
            if row["task"] != "classify_vulns":
                continue
            uid, snippet = row["id"], row["input"]
            prompt = make_prompt(uid, snippet)

            try:
                raw = ask(prompt)
            except Exception as e:
                print(f"[warn] request fail {uid}: {e}", file=sys.stderr)
                rows.append({"id": uid, "pred": {"labels": [], "primary_severity": "Informational"}})
                fails += 1
                continue

            # dump raw for debug
            with open(f"eval_debug/{uid}.txt","w") as dbg:
                dbg.write(raw)

            raw2 = continue_if_incomplete(raw, prompt)

            try:
                obj = coerce_json(raw2)
                pred = normalize(obj)
            except Exception as e:
                print(f"[warn] parse fail {uid}: {e}", file=sys.stderr)
                pred = {"labels": [], "primary_severity": "Informational"}
                fails += 1

            rows.append({"id": uid, "pred": pred})

    with open("eval_preds.jsonl","w") as out:
        for r in rows:
            out.write(json.dumps(r)+"\n")

    print(f"[ok] wrote {len(rows)} predictions to eval_preds.jsonl; fails={fails}")

if __name__ == "__main__":
    main()
