# IndicGenBench — XQuAD-IN (Extractive QA)

### Paper

Title: `IndicGenBench: A Multilingual Benchmark to Evaluate Generation Capabilities of LLMs on Indic Languages`
Abstract: https://arxiv.org/abs/2404.16816

IndicGenBench is a multilingual benchmark evaluating LLM generation capabilities across Indic languages. **XQuAD-IN** is the extractive reading comprehension component, adapted from XQuAD with human translations into Indic languages. Given a passage and a question (both in the target language), the model must extract a short answer span.

Dataset: https://huggingface.co/datasets/google/IndicGenBench_xquad_in

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

* `indicgenbench_xquad_in`: All 11 language tasks aggregated (weighted mean by size).

#### Tasks

* `indicgenbench_xquad_in_bn` through `indicgenbench_xquad_in_ur` (11 tasks)

---

## Running the Task

### Prerequisites

```bash
pip install lm-eval
```

### Example Usage

**Run all 11 languages:**

```bash
lm_eval --model hf \
    --model_args pretrained=sarvamai/sarvam-1 \
    --tasks indicgenbench_xquad_in \
    --num_fewshot 0 \
    --batch_size auto \
    --output_path results/sarvam-1_xquad_in
```

**Run a single language (Hindi):**

```bash
lm_eval --model hf \
    --model_args pretrained=sarvamai/sarvam-1 \
    --tasks indicgenbench_xquad_in_hi \
    --num_fewshot 0 \
    --batch_size auto \
    --output_path results/sarvam-1_xquad_in_hi
```

---

### Notes

- Uses the `validation` split (the only available split) for evaluation. Few-shot examples are also drawn from this split when `num_fewshot > 0` — zero-shot (`--num_fewshot 0`) is recommended to avoid contamination.
- The dataset is loaded using `field="examples"` to unwrap the top-level canary wrapper in the JSON files.
- Metrics: `exact_match` and `f1` (squad-style token-level, higher is better).
- Language filtering is done at load time via `process_docs` on the `lang` column.
