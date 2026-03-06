# IndicGenBench — FLORES-IN (Translation)

### Paper

Title: `IndicGenBench: A Multilingual Benchmark to Evaluate Generation Capabilities of LLMs on Indic Languages`
Abstract: https://arxiv.org/abs/2404.16816

**FLORES-IN** is the machine translation component of IndicGenBench, based on the FLORES-200 benchmark extended to 29 Indic languages. Two translation directions are provided as separate task groups:

- **`enxx`** — English → Indic language
- **`xxen`** — Indic language → English

Dataset: https://huggingface.co/datasets/google/IndicGenBench_flores_in

### Supported Languages

| Code | Language  |
|------|-----------|
| `bn` | Bengali   |
| `gu` | Gujarati  |
| `hi` | Hindi     |
| `kn` | Kannada   |
| `ml` | Malayalam |
| `mr` | Marathi   |
| `or` | Odia      |
| `pa` | Punjabi   |
| `ta` | Tamil     |
| `te` | Telugu    |
| `ur` | Urdu      |

### Citation

```
@inproceedings{indicgenbench2024,
  title     = {IndicGenBench: A Multilingual Benchmark to Evaluate Generation Capabilities of LLMs on Indic Languages},
  author    = {Harman Singh and Nitish Gupta and Shikhar Bharadwaj and Dinesh Tewari and Partha Talukdar},
  booktitle = {Proceedings of ACL 2024},
  year      = {2024}
}
```

### Groups and Tasks

#### Groups

* `indicgenbench_flores_in_enxx`: English → Indic (11 tasks)
* `indicgenbench_flores_in_xxen`: Indic → English (11 tasks)

#### Tasks

* `indicgenbench_flores_in_enxx_{lang}` — e.g., `indicgenbench_flores_in_enxx_hi`
* `indicgenbench_flores_in_xxen_{lang}` — e.g., `indicgenbench_flores_in_xxen_hi`

---

## Running the Task

### Prerequisites

```bash
pip install lm-eval evaluate
pip install sacrebleu  # for BLEU and chrF
```

### Example Usage

**English → all 11 Indic languages:**

```bash
lm_eval --model hf \
    --model_args pretrained=sarvamai/sarvam-1 \
    --tasks indicgenbench_flores_in_enxx \
    --num_fewshot 5 \
    --batch_size auto \
    --output_path results/sarvam-1_flores_enxx
```

**All 11 Indic languages → English:**

```bash
lm_eval --model hf \
    --model_args pretrained=sarvamai/sarvam-1 \
    --tasks indicgenbench_flores_in_xxen \
    --num_fewshot 5 \
    --batch_size auto \
    --output_path results/sarvam-1_flores_xxen
```

**Single direction, single language (Hindi → English):**

```bash
lm_eval --model hf \
    --model_args pretrained=sarvamai/sarvam-1 \
    --tasks indicgenbench_flores_in_xxen_hi \
    --num_fewshot 5 \
    --batch_size auto \
    --output_path results/sarvam-1_flores_xxen_hi
```

---

### Notes

- `test` split (FLORES devtest) is used for evaluation; `validation` (FLORES dev) is used for few-shot examples.
- The dataset is loaded using `field="examples"` to unwrap the top-level canary wrapper. If this fails, try `dataset_name: "examples"` as an alternative.
- Language + direction filtering is done via `process_docs` on the `lang` and `translation_direction` columns.
- Metrics: `bleu` and `chrf` (via HuggingFace `evaluate` library, higher is better).
- Requires `sacrebleu` (`pip install sacrebleu`) for the evaluate library's BLEU and chrF backends.
