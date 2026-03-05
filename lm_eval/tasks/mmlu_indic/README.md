# MMLU Indic

### Paper

Title: `Measuring Massive Multitask Language Understanding`
Abstract: https://arxiv.org/abs/2009.03300

MMLU is a benchmark covering 57 subjects across STEM, humanities, social sciences, and more. This Indic variant (`sarvamai/mmlu-indic`) provides translations into 10 Indic languages.

Dataset: https://huggingface.co/datasets/sarvamai/mmlu-indic

### Supported Languages

| Code | Language   |
|------|------------|
| `bn` | Bengali    |
| `gu` | Gujarati   |
| `hi` | Hindi      |
| `kn` | Kannada    |
| `ml` | Malayalam  |
| `mr` | Marathi    |
| `or` | Odia       |
| `pa` | Punjabi    |
| `ta` | Tamil      |
| `te` | Telugu     |

### Citation

```
@article{hendryckstest2021,
  author    = {Dan Hendrycks and Collin Burns and Steven Basart and Andy Zou and Mantas Mazeika and Dawn Song and Jacob Steinhardt},
  title     = {Aligning AI With Shared Human Values},
  journal   = {Proceedings of the International Conference on Learning Representations (ICLR)},
  year      = {2021}
}
```

### Groups and Tasks

#### Groups

* `mmlu_indic`: All 10 language tasks aggregated (weighted mean by size).

#### Tasks

* `mmlu_indic_bn`: Bengali
* `mmlu_indic_gu`: Gujarati
* `mmlu_indic_hi`: Hindi
* `mmlu_indic_kn`: Kannada
* `mmlu_indic_ml`: Malayalam
* `mmlu_indic_mr`: Marathi
* `mmlu_indic_or`: Odia
* `mmlu_indic_pa`: Punjabi
* `mmlu_indic_ta`: Tamil
* `mmlu_indic_te`: Telugu

---

## Running the Task

### Prerequisites

```bash
pip install lm-eval
# or, from source:
git clone https://github.com/EleutherAI/lm-evaluation-harness
cd lm-evaluation-harness
pip install -e .
```

---

### Example: sarvamai/sarvam-1

**Run all 10 Indic languages (full benchmark):**

```bash
lm_eval --model hf \
    --model_args pretrained=sarvamai/sarvam-1 \
    --tasks mmlu_indic \
    --num_fewshot 5 \
    --batch_size auto \
    --output_path results/sarvam-1_mmlu_indic
```

**Run a single language (Hindi):**

```bash
lm_eval --model hf \
    --model_args pretrained=sarvamai/sarvam-1 \
    --tasks mmlu_indic_hi \
    --num_fewshot 5 \
    --batch_size auto \
    --output_path results/sarvam-1_mmlu_indic_hi
```

**Quick smoke-test (10 examples, no GPU required):**

```bash
lm_eval --model hf \
    --model_args pretrained=sarvamai/sarvam-1 \
    --tasks mmlu_indic_hi \
    --num_fewshot 5 \
    --batch_size 4 \
    --limit 10 \
    --output_path results/sarvam-1_mmlu_indic_hi_debug
```

**Run with bfloat16 precision (recommended for large GPUs):**

```bash
lm_eval --model hf \
    --model_args pretrained=sarvamai/sarvam-1,dtype=bfloat16 \
    --tasks mmlu_indic \
    --num_fewshot 5 \
    --batch_size auto \
    --output_path results/sarvam-1_mmlu_indic
```

**Run with vLLM backend (faster inference):**

```bash
lm_eval --model vllm \
    --model_args pretrained=sarvamai/sarvam-1,dtype=bfloat16 \
    --tasks mmlu_indic \
    --num_fewshot 5 \
    --batch_size auto \
    --output_path results/sarvam-1_mmlu_indic
```

**Run a subset of languages:**

```bash
lm_eval --model hf \
    --model_args pretrained=sarvamai/sarvam-1 \
    --tasks mmlu_indic_hi,mmlu_indic_bn,mmlu_indic_ta \
    --num_fewshot 5 \
    --batch_size auto \
    --output_path results/sarvam-1_mmlu_indic_subset
```

---

### Notes

- Evaluation uses the `test` split (~14,000 examples per language); few-shot examples are drawn from `validation` (~280 examples per language).
- The task uses `multiple_choice` output type with 4 options (A/B/C/D).
- Metrics reported: `acc` and `acc_norm` (mean, higher is better).
- Few-shot examples are sampled using the `first_n` sampler from the validation split.
- Romanized variants (e.g., `hi_roman`) are not included in this task.
