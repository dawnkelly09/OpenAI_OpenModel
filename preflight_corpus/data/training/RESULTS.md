# Evaluating gpt-oss:20b performance

## Introduction

The end-goal of FirstPass is an agent which can evaluate Solidity smart contracts, identify security vulnerabilities, properly classify severity, and output a report that a smart contract developer can use as a screening tool prior to a professional audit. In order to fine-tune gpt-oss:20b, a dataset was created to identify vulnerability patterns, classify severity, and demonstrate buggy and fixed code example pairs. An evaluation of the model's performance of the task prior to adding any training or tools was completed in order to evaluate the effectiveness of the fine-tuning. That process, and related findings, are described in the following sections.

## Testing Methods - Baseline Evaluation

The model was provided with a list of 15 test inquiries which are located in `preflight_corpus/data/eval/eval_items.csv`. The test evaluation script `run_baseline_eval_stream.py` uses the prompt located in `preflight_corpus/data/eval/system_security.txt` and asks the model to return values for label(s) and a single primary severity. The intention was to evaluate how effectively the model could identify and classify Solidity vulnerabilites prior to any fine-tune or making a RAG structure available.

```
PROMPT: Do NOT show your reasoning. Output ONLY:
{"labels":[...], "primary_severity":"..."}
Use labels EXACTLY from this set:
[Reentrancy, Access Control, Authorization Bypass, ERC Conformance, Integer Overflow/Underflow, Unchecked Call, Delegatecall Misuse, Oracle Manipulation, Timestamp Dependence, tx.origin Misuse, Insecure Randomness, DoS via Unbounded Loop, DoS via Unexpected Revert, Front-Running / MEV, Arithmetic/Overflow, Storage Collision, Signature Replay, Signature Malleability, Permit/Signature Misuse, Fee-On-Transfer Token Misaccounting, Slippage Misuse, Broken Invariant, Gas Griefing, Precision / Reward Accounting, Proxy/Clones|Deployment, Upgradeability|ERC Conformance, Allowance Race, Bypass Pause / Circuit Breaker]
```

Sample evaluation item:
```
classify_vulns,eval-oz-erc20-allowance-rot,"function changeAllowance(address s,uint256 v) external { _allowances[msg.sender][s]=v; }",,,,,"",,"solidity,openzeppelin,eval"
```

## Baseline Findings

After some false starts requiring tweaking of scripting to cure time out errors, the model returned the following output, indicating a successful run:

```bash
[ok] wrote 15 predictions to eval_preds.jsonl; fails=0
```

This initial batch of predictions is available at `preflight_corpus/data/eval/eval_preds.jsonl`.

Sample prediction from baseline evaluation:
```
{"id": "eval-oz-erc20-allowance-rot", "pred": {"labels": ["Allowance Race"], "primary_severity": "Medium"}}
```

Next, `score_eval.py` was used to evaluate model performance at the requested task. The initial report was as follows:

=== Baseline Scoring ===
Items evaluated: 15
Labels (macro over items) → Precision: 0.50  Recall: 0.43  F1: 0.46
Severity accuracy: 0.47
Empty label predictions: 6/15 (40.00%)

=== Per-label Precision/Recall/F1 (support ≥ 1 in gold) ===
Label                                   Sup   TP   FP   FN       P      R     F1
Access Control                            3    0    1    3    0.00   0.00   0.00
Authorization Bypass                      3    0    1    3    0.00   0.00   0.00
ERC Conformance                           3    0    0    3    0.00   0.00   0.00
Allowance Race                            1    1    0    0    1.00   1.00   1.00
Bypass Pause / Circuit Breaker            1    1    0    0    1.00   1.00   1.00
Delegatecall Misuse                       1    1    0    0    1.00   1.00   1.00
DoS via Unbounded Loop                    1    1    0    0    1.00   1.00   1.00
Insecure Randomness                       1    1    0    0    1.00   1.00   1.00
Storage Collision                         1    1    0    0    1.00   1.00   1.00
Unchecked Call                            1    1    0    0    1.00   1.00   1.00
tx.origin Misuse                          1    1    0    0    1.00   1.00   1.00
Arithmetic/Overflow                       1    0    0    1    0.00   0.00   0.00
Fee-On-Transfer Token Misaccounting       1    0    0    1    0.00   0.00   0.00
Oracle Manipulation                       1    0    0    1    0.00   0.00   0.00
Slippage Misuse                           1    0    0    1    0.00   0.00   0.00

=== Severity Confusions (Gold → Pred) ===
High           → Informational  : 3
Medium         → Informational  : 3
Medium         → High           : 1
Low            → High           : 1

## Baseline Analysis

This is my first time working with this sort of data evaluation and I did lean heavily on ChatGPT for this evaluation and analysis portion. As I understand things, the F1, precision, and recall scores are inline for what is expected on a "zero-shot" evaluation of this model. The model also performed better at recognizing the most common vulnerabilities (such as "Allowance Race") and less so with more abstract vulnerabilities which don't have as many concrete examples available online. 

It does seem clear some fine-tuning with explicit buggy versus fixed code examples added to focus on less common, but still serious, vulnerabilities should improve performance in detecting and classifying vulnerabilities. Specific training around severity rubrics should also help the model improve in it's ability to assign severity to vulnerabilities once they are detected.

## Fine Tuning

The `seed_examples.jsonl` was split into three files (train, eval, and test) to facilitate creation of Supervised Fine-Tuning (SFT) prompt-response pairs for training the model via demonstration of desired correct responses. The `render_sft.py` script was used to ingest the `seed_examples.jsonl` rows and write corresponding prompt/response pairs for training. 

- **`preflight-sft` Dataset on Hugging Face**: https://huggingface.co/datasets/dawnkelly09/preflight-sft

This was the point at which I discovered, due to hardware and budgetary constraints, I would not be able to actually train the `gpt-oss:20b` model. Rather than give up entirely, I opted to validate the training pipeline using Hugging Face and a lighter model.

- **Preflight Train Space on Hugging Face**: https://huggingface.co/spaces/dawnkelly09/preflight-train

On a T4 I fine-tuned SmolLM2-1.7B with QLoRA and reduced validation perplexity from 22.78 → 13.87 (−39%), corresponding to a loss drop of 0.496 nats/token.

Under the same data and adapter recipe, I expect a comparable loss reduction on `gpt-oss-20b`. In practice that means: loss_after(20B) ≈ loss_before(20B) − 0.496 (equivalently, ppl_after(20B) ≈ 0.61 × ppl_before(20B)).

Larger models are typically at least as sample-efficient, so absolute post-train performance should be better (lower ppl, higher downstream scores), though the relative percentage drop can vary with optimization details.

## Evaluating Training Outcome

The effectiveness of the training was evaluated on a held-out validation split using a teacher forcing technique of feeding true tokens in, asking the model "What probability do you assign to the next true token?", and using that feedback to determine loss and exponentiate perplexity.

- **Model**: SmolLM2-1.7B
- **Before fine-tune**: loss = 3.1259, ppl = 22.78
- **After fine-tune**: loss = 2.6296, ppl = 13.87
- **Perplexity factor**: 13.87 / 22.78 ≈ 0.61 => -39% ppl

As I understand this data, the SmolLM2-1.7B model's 39% decrease in validation perplexity translates to the model being far less "surprised" (loss) by smart contract vulnerability domain text than prior to training. Using the same data and LoRA recipe should translate to materially better next-token predictions on domain data in larger models. Training details would drive final numbers but, it feels reasonable to expect similar direction and scale of gain with the larger gpt-oss:20b model. 