# MILU

### Paper

Title: `MILU: A Multi-task Indic Language Understanding Benchmark`
Abstract: https://arxiv.org/abs/2411.02538

MILU is a comprehensive evaluation benchmark for Large Language Models across 11 Indic languages. It contains approximately 80,000 multiple-choice questions spanning 8 domains and 41 subjects, with content sourced from regional and state-level Indian examinations to reflect both general and culturally specific knowledge.

Dataset: https://huggingface.co/datasets/ai4bharat/MILU

> **Note**: This is a gated dataset. You must request access on HuggingFace and authenticate with `huggingface-cli login` (or set `HF_TOKEN`) before running these tasks.

### Supported Languages

| Code | Language   | Test Questions |
|------|------------|---------------|
| `bn` | Bengali    | 6,638         |
| `en` | English    | 13,536        |
| `gu` | Gujarati   | 4,827         |
| `hi` | Hindi      | 14,837        |
| `kn` | Kannada    | 6,234         |
| `ml` | Malayalam  | 4,321         |
| `mr` | Marathi    | 6,924         |
| `or` | Odia       | 4,525         |
| `pa` | Punjabi    | 4,099         |
| `ta` | Tamil      | 6,372         |
| `te` | Telugu     | 7,304         |

### Domains

Arts & Humanities, Business Studies, Engineering & Tech, Environmental Sciences, Health & Medicine, Law & Governance, Science, Social Sciences

### Citation

```
@misc{milu2024,
  title  = {MILU: A Multi-task Indic Language Understanding Benchmark},
  author = {Sshubam Verma and Mohammed Safi Ur Rahman Khan and Vishwa Shah and Varsha Ramesh and Utkarsh Venaik and Rudra Murthy and Raj Dabre and Vivek Seshadri and Anoop Kunchukuttan and Pratyush Kumar},
  year   = {2024},
  eprint = {2411.02538},
  archivePrefix = {arXiv}
}
```

### Groups and Tasks

#### Groups

* `milu`: All 11 language tasks aggregated (weighted mean by size).

#### Tasks

* `milu_bn`: Bengali
* `milu_en`: English
* `milu_gu`: Gujarati
* `milu_hi`: Hindi
* `milu_kn`: Kannada
* `milu_ml`: Malayalam
* `milu_mr`: Marathi
* `milu_or`: Odia
* `milu_pa`: Punjabi
* `milu_ta`: Tamil
* `milu_te`: Telugu

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

Authenticate with HuggingFace (required — gated dataset):

```bash
huggingface-cli login
# or: export HF_TOKEN=<your_token>
```

---

### Example Usage

**Run all 11 languages (full benchmark):**

```bash
lm_eval --model hf \
    --model_args pretrained=sarvamai/sarvam-1 \
    --tasks milu \
    --num_fewshot 5 \
    --batch_size auto \
    --output_path results/sarvam-1_milu
```

**Run a single language (Hindi):**

```bash
lm_eval --model hf \
    --model_args pretrained=sarvamai/sarvam-1 \
    --tasks milu_hi \
    --num_fewshot 5 \
    --batch_size auto \
    --output_path results/sarvam-1_milu_hi
```

**Quick smoke-test (10 examples, no GPU required):**

```bash
lm_eval --model hf \
    --model_args pretrained=sarvamai/sarvam-1 \
    --tasks milu_hi \
    --num_fewshot 5 \
    --batch_size 4 \
    --limit 10 \
    --output_path results/sarvam-1_milu_hi_debug
```

**Run with bfloat16 precision:**

```bash
lm_eval --model hf \
    --model_args pretrained=sarvamai/sarvam-1,dtype=bfloat16 \
    --tasks milu \
    --num_fewshot 5 \
    --batch_size auto \
    --output_path results/sarvam-1_milu
```

**Run with vLLM backend:**

```bash
lm_eval --model vllm \
    --model_args pretrained=sarvamai/sarvam-1,dtype=bfloat16 \
    --tasks milu \
    --num_fewshot 5 \
    --batch_size auto \
    --output_path results/sarvam-1_milu
```

---

### Notes

- Evaluation uses the `test` split (~79,617 total questions); few-shot examples are drawn from the `validation` split (8,933 examples).
- The task uses `multiple_choice` output type with 4 options (A/B/C/D).
- The `target` column contains string labels (`"option1"`–`"option4"`); these are converted to integer indices (0–3) for scoring.
- Metrics reported: `acc` and `acc_norm` (mean, higher is better).
- Few-shot examples are sampled using the `first_n` sampler from the validation split.
- The dataset is loaded via `data_dir` (full language name, e.g., `"Hindi"`) rather than a config name.
