# IndicGenBench — XOrQA-IN (Cross-lingual QA)

### Paper

Title: `IndicGenBench: A Multilingual Benchmark to Evaluate Generation Capabilities of LLMs on Indic Languages`
Abstract: https://arxiv.org/abs/2404.16816

**XOrQA-IN** is the cross-lingual question answering component of IndicGenBench, adapted from the XOR-TyDi QA benchmark. The passage is in **English**, the question is in the target **Indic language**, and the expected answer is also in the Indic language (`translated_answers`). This tests a model's ability to perform cross-lingual reading comprehension.

Dataset: https://huggingface.co/datasets/google/IndicGenBench_xorqa_in

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

* `indicgenbench_xorqa_in`: All 11 language tasks aggregated (weighted mean by size).

#### Tasks

* `indicgenbench_xorqa_in_bn` through `indicgenbench_xorqa_in_ur` (11 tasks)

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
    --tasks indicgenbench_xorqa_in \
    --num_fewshot 0 \
    --batch_size auto \
    --output_path results/sarvam-1_xorqa_in
```

**Run a single language (Hindi):**

```bash
lm_eval --model hf \
    --model_args pretrained=sarvamai/sarvam-1 \
    --tasks indicgenbench_xorqa_in_hi \
    --num_fewshot 0 \
    --batch_size auto \
    --output_path results/sarvam-1_xorqa_in_hi
```

---

### Notes

- Uses the `validation` split for both evaluation and few-shot examples. Zero-shot (`--num_fewshot 0`) is recommended to avoid contamination.
- The dataset is loaded using `field="examples"` to unwrap the top-level canary wrapper.
- **Cross-lingual setup**: the passage (`context`) is in English; the question is in the target Indic language; evaluation is against `translated_answers` (human-translated Indic answers).
- Metrics: `exact_match` and `f1` (squad-style token-level, higher is better).
- Language filtering is done at load time via `process_docs` on the `lang` column.
