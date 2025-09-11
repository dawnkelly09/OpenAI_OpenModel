# PreFlight Audit — Solidity Contract Analyzer (SmolLM2 + LoRA)

Note: this started as an effort to work locally with OpenAI's gpt-oss:20b open source model. You can see the baseline eval [here](https://github.com/dawnkelly09/OpenAI_OpenModel/blob/c507539b7a9bde3e96f10ed8fd02dc1c7dc7a869/preflight_corpus/data/eval/run_baseline_eval_stream.py#L3C1-L3C22). Ultimately, I learned I could not train this model due to hardware constraints, so I decided to validate the pipleline instead. 

PreFlight Audit is a tiny web app + API that analyzes Solidity contracts and returns a structured security report (JSON + readable Markdown).

It uses a small open-weights base model (SmolLM2-1.7B-Instruct) and can optionally attach a LoRA adapter fine-tuned on auditing data.

🚀 Live demo (Hugging Face Space): https://huggingface.co/spaces/dawnkelly09/preflight-train

📦 Source: https://github.com/dawnkelly09/OpenAI_OpenModel

## What it does

Given a pasted or uploaded .sol file, PreFlight:

Runs lightweight static checks (regex-based signals like tx.origin, delegatecall, unbounded loops, etc.).

Performs a RAG-lite fetch from a local KB (optional .md / .txt files) using simple lexical overlap.

Builds a compact prompt with context + code and asks the model for JSON only.

Parses/validates the JSON and renders a Markdown summary alongside the raw JSON.

### The JSON schema

{
  "summary": "one paragraph",
  "findings": [
    { "title": "Issue", "severity": "Low|Medium|High|Critical|Informational",
      "evidence": "code snippet or description",
      "remediation": "actionable fix"
    }
  ],
  "overall_risk": "Informational|Low|Medium|High|Critical"
}

## Using the Space (end-users)

Open the Space: https://huggingface.co/spaces/dawnkelly09/preflight-train

Paste Solidity into the textarea, or upload a .sol/.txt file.

Click Analyze.
You’ll see:

- a Markdown report (summary + findings).

- the Raw JSON/Text block you can copy into your tooling.

*Tip*: large contracts on CPU can take a bit. 

## Deploying on your own Hugging Face Space (maintainers)

The repo is set up for a Docker Space.

Create a new Space → SDK: Docker → connect this GitHub repo.

(Optional) Hardware

CPU Basic works for demos (slower).

GPU (e.g., T4) is much faster and enables 4-bit QLoRA automatically.

## Environment variables (Settings → Variables):

BASE_MODEL (default: HuggingFaceTB/SmolLM2-1.7B-Instruct)

ADAPTER_ID (default: dawnkelly09/preflight-smollm2-1.7b-lora)

USE_ADAPTER → 1 to enable the LoRA, 0 to use base model only

CPU_ONLY → 1 to force CPU path (Spaces CPU images set this internally)

MAX_NEW_TOKENS (default 512), TEMPERATURE (default 0.2), TOP_P (default 0.9)

KB_DIR path with .md/.txt resources (default /app/kb)

Commit/push. The Space will build and serve the app on port 7860.

## Run locally (Docker)

1. Clone
git clone https://github.com/dawnkelly09/OpenAI_OpenModel
cd OpenAI_OpenModel

2. Build
docker build -t preflight .

3. Run (CPU example, LoRA enabled)
docker run --rm -p 7860:7860 \
  -e USE_ADAPTER=1 \
  -e CPU_ONLY=1 \
  preflight

4. Visit http://localhost:7860


GPU (Docker host with NVIDIA drivers): drop CPU_ONLY, and ensure NVIDIA runtime is available:

docker run --rm -p 7860:7860 --gpus all \
  -e USE_ADAPTER=1 \
  preflight

## Run locally (Python, no Docker)

For quick hacking. You’ll need Python 3.10+.

```
python -m venv .venv && source .venv/bin/activate
pip install --upgrade pip
```

### Core deps

```
pip install "fastapi==0.111.*" "uvicorn[standard]==0.30.*" python-multipart==0.0.9
pip install "transformers>=4.44" "peft>=0.10.0" datasets accelerate huggingface_hub
```

### CPU path:

```
pip install torch==2.4.0
```

### (Optional) GPU + 4-bit QLoRA:

```
pip install --index-url https://download.pytorch.org/whl/cu121 "torch==2.4.0+cu121" bitsandbytes==0.43.3

export USE_ADAPTER=1
uvicorn app:app --host 0.0.0.0 --port 7860
```

## API
- **POST /analyze**:

Request:

```
POST /analyze
Content-Type: application/json

{ "code_text": "pragma solidity ^0.8.20; contract X { ... }" }
```

Successful response:

```
{
  "markdown": "### Preflight Report\n...",
  "json": {
    "summary": "…",
    "findings": [ { "title": "tx.origin Misuse", "severity": "High", ... } ],
    "overall_risk": "Medium"
  }
}
```

If the model didn’t return valid JSON, you’ll get:

```
{ "markdown": "...", "raw": "original text" }
```

- **GET /**:

Minimal HTML page for paste/upload + “Analyze” button.

```
GET /health
```

Returns { "ok": true }.

## Configuration

Env Var ------- | 	---------- Default ------------ | What it does ----- </br>
`BASE_MODEL`	| HuggingFaceTB/SmolLM2-1.7B-Instruct  | Base causal LM</br>
`ADAPTER_ID`  | dawnkelly09/preflight-smollm2-1.7b-lora | LoRA adapter repo id </br>
`USE_ADAPTER` | 1	  | Attach LoRA if 1, otherwise run base model </br>
`CPU_ONLY`	| 0	  | Force CPU path if 1 </br>
`MAX_NEW_TOKENS`	| 512	| Generation cap. Lower = faster </br>
`TEMPERATURE`	| 0.2	| Sampling temperature (we default to greedy for best JSON) </br>
`TOP_P`	| 0.9 |	Nucleus sampling (unused when greedy)</br>
`KB_DIR`	| /app/kb	| Folder with .md / .txt files for RAG-lite

## Built-in static checks (quick signals)

`tx.origin` misuse (High)

`delegatecall` misuse (High)

`selfdestruct` / `suicide` (Medium)

Unchecked low-level calls (`.call`, `.send`, `.transfer`) (Medium)

Block attributes as randomness (Low)

Unbounded loops (Low)

ERC-20 approval race (approve) (Medium)

Pausable patterns present; ensure correct guarding (Medium)

*These are hints, not verdicts; the model combines them with the source to produce the final JSON report.*

## Notes & Troubleshooting

### Empty {} output

- Make sure `USE_ADAPTER=1` if you want the fine-tuned head.

Ensure your adapter’s base matches `BASE_MODEL`.

Large inputs on CPU can hit timeouts—trim the code or reduce `MAX_NEW_TOKENS`.

### `bitsandbytes` warning on CPU

- **“Compiled without GPU support”**: Safe to ignore on CPU; QLoRA is only used on GPU.

### Newer PEFT configs

If your adapter config includes unknown keys (e.g., `corda_config`), the app automatically sanitizes and retries.

## Speed tips

Prefer GPU Spaces, or lower `MAX_NEW_TOKENS` (e.g., 256).

Keep greedy decoding (more reliable JSON).

RAG files in `KB_DIR` should be concise; the app already truncates long context.

## Roadmap (nice-to-haves)

- Better retrieval (embeddings + vector index).

- Multi-file projects (import/library resolution).

- Etherscan/chain fetch for deployed contracts.

- Export report as PDF.

- CI test set for regression checks.

## Acknowledgements

- Base model: SmolLM2-1.7B-Instruct

- Finetuning / adapters: PEFT / LoRA

- Inference stack: Transformers, FastAPI, Uvicorn

- Hosting: Hugging Face Spaces

- AI Coding Assistance: GPT-5 Thinking model

License

This repo uses the license included in the repository (see LICENSE).
Model and dataset licenses apply to their respective sources.
