# IndicGenBench — CrossSum-IN (Cross-lingual Summarization)

### Paper

Title: `IndicGenBench: A Multilingual Benchmark to Evaluate Generation Capabilities of LLMs on Indic Languages`
Abstract: https://arxiv.org/abs/2404.16816

**CrossSum-IN** is the cross-lingual summarization component of IndicGenBench. Given an English news article, the model must generate a summary in the target Indic language. The benchmark is adapted from CrossSum with human translations into Indic languages.

Dataset: https://huggingface.co/datasets/google/IndicGenBench_crosssum_in

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

* `indicgenbench_crosssum_in`: All 11 language tasks aggregated (weighted mean by size).

#### Tasks

* `indicgenbench_crosssum_in_bn` through `indicgenbench_crosssum_in_ur` (11 tasks)

---

## Running the Task

### Prerequisites

```bash
pip install lm-eval evaluate
pip install rouge-score  # for ROUGE-L backend
```

### Example Usage

**Run all 11 languages:**

```bash
lm_eval --model hf \
    --model_args pretrained=sarvamai/sarvam-1 \
    --tasks indicgenbench_crosssum_in \
    --num_fewshot 0 \
    --batch_size auto \
    --output_path results/sarvam-1_crosssum_in
```

**Run a single language (Hindi):**

```bash
lm_eval --model hf \
    --model_args pretrained=sarvamai/sarvam-1 \
    --tasks indicgenbench_crosssum_in_hi \
    --num_fewshot 0 \
    --batch_size auto \
    --output_path results/sarvam-1_crosssum_in_hi
```

---

### Notes

- Uses the `validation` split for both evaluation and few-shot examples. Zero-shot (`--num_fewshot 0`) is recommended to avoid contamination.
- The dataset is loaded using `field="examples"` to unwrap the top-level canary wrapper.
- The model sees an English article and must output a summary in the target Indic language.
- Metric: `rougeL` (via HuggingFace `evaluate` library, higher is better).
- Requires `rouge-score` (`pip install rouge-score`) for the evaluate library backend.
