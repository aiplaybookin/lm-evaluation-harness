# ARC Challenge Indic

### Paper

Title: `Think you have Solved Question Answering? Try ARC, the AI2 Reasoning Challenge`
Abstract: https://arxiv.org/abs/1803.05457

ARC Challenge is a set of genuine grade-school level, multiple-choice science questions requiring reasoning beyond simple retrieval. This Indic variant (`sarvamai/arc-challenge-indic`) provides translations into 10 Indic languages plus English.

Dataset: https://huggingface.co/datasets/sarvamai/arc-challenge-indic

### Supported Languages

| Code | Language   |
|------|------------|
| `bn` | Bengali    |
| `en` | English    |
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
@article{Clark2018ThinkYH,
  title     = {Think you have Solved Question Answering? Try ARC, the AI2 Reasoning Challenge},
  author    = {Peter Clark and Isaac Cowhey and Oren Etzioni and Tushar Khot and Ashish Sabharwal and Carissa Schoenick and Oyvind Tafjord},
  journal   = {ArXiv},
  year      = {2018},
  volume    = {abs/1803.05457}
}
```

### Groups and Tasks

#### Groups

* `arc_challenge_indic`: All 11 language tasks aggregated (weighted mean by size).

#### Tasks

* `arc_challenge_indic_bn`: Bengali
* `arc_challenge_indic_en`: English
* `arc_challenge_indic_gu`: Gujarati
* `arc_challenge_indic_hi`: Hindi
* `arc_challenge_indic_kn`: Kannada
* `arc_challenge_indic_ml`: Malayalam
* `arc_challenge_indic_mr`: Marathi
* `arc_challenge_indic_or`: Odia
* `arc_challenge_indic_pa`: Punjabi
* `arc_challenge_indic_ta`: Tamil
* `arc_challenge_indic_te`: Telugu

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

**Run all 11 languages (full benchmark):**

```bash
lm_eval --model hf \
    --model_args pretrained=sarvamai/sarvam-1 \
    --tasks arc_challenge_indic \
    --num_fewshot 25 \
    --batch_size auto \
    --output_path results/sarvam-1_arc_challenge_indic
```

**Run a single language (Hindi):**

```bash
lm_eval --model hf \
    --model_args pretrained=sarvamai/sarvam-1 \
    --tasks arc_challenge_indic_hi \
    --num_fewshot 25 \
    --batch_size auto \
    --output_path results/sarvam-1_arc_challenge_indic_hi
```

**Quick smoke-test (10 examples):**

```bash
lm_eval --model hf \
    --model_args pretrained=sarvamai/sarvam-1 \
    --tasks arc_challenge_indic_hi \
    --num_fewshot 5 \
    --batch_size 4 \
    --limit 10 \
    --output_path results/sarvam-1_arc_challenge_indic_hi_debug
```

**Run with bfloat16 precision (recommended for large GPUs):**

```bash
lm_eval --model hf \
    --model_args pretrained=sarvamai/sarvam-1,dtype=bfloat16 \
    --tasks arc_challenge_indic \
    --num_fewshot 25 \
    --batch_size auto \
    --output_path results/sarvam-1_arc_challenge_indic
```

**Run with vLLM backend (faster inference):**

```bash
lm_eval --model vllm \
    --model_args pretrained=sarvamai/sarvam-1,dtype=bfloat16 \
    --tasks arc_challenge_indic \
    --num_fewshot 25 \
    --batch_size auto \
    --output_path results/sarvam-1_arc_challenge_indic
```

**Run Indic-only languages (excluding English):**

```bash
lm_eval --model hf \
    --model_args pretrained=sarvamai/sarvam-1 \
    --tasks arc_challenge_indic_bn,arc_challenge_indic_gu,arc_challenge_indic_hi,arc_challenge_indic_kn,arc_challenge_indic_ml,arc_challenge_indic_mr,arc_challenge_indic_or,arc_challenge_indic_pa,arc_challenge_indic_ta,arc_challenge_indic_te \
    --num_fewshot 25 \
    --batch_size auto \
    --output_path results/sarvam-1_arc_challenge_indic_only
```

---

### Notes

- Evaluation uses the `test` split (~1,150 examples per language); few-shot examples are drawn from `validation` (~294 examples per language).
- The task uses `multiple_choice` output type with 4 options (A/B/C/D).
- The `answerKey` column contains letter labels (`"A"`–`"D"`); these are converted to integer indices (0–3) for scoring.
- The `choices` column is a dict with `.text` and `.label` sub-fields.
- Metrics reported: `acc` and `acc_norm` (mean, higher is better).
- Few-shot examples are sampled using the `first_n` sampler from the validation split.
