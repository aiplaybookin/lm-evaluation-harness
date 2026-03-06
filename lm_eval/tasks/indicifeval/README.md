# IndicIFEval

### Paper

Title: `IndicIFEval: Multilingual Instruction Following Evaluation for Indic Languages`

IndicIFEval adapts the original English IFEval benchmark to 14 Indic languages. It evaluates instruction-following using **automatically verifiable, rule-based constraints** (keyword frequency, word/paragraph count, start/end phrases, etc.) — the same constraint types as the original IFEval, making cross-lingual comparison straightforward.

Dataset: https://huggingface.co/datasets/ai4bharat/IndicIFEval

### Two Configs

| Config | Description | Languages | Size |
|--------|-------------|-----------|------|
| `indicifeval-ground` | Synthetically generated instructions grounded in native Indic content | 14 | ~5.17k |
| `indicifeval-trans` | Translated & localized from the original English IFEval; manually verified | 15 (incl. English) | ~7.35k |

### Supported Languages

| Code | Language   | Ground | Trans |
|------|------------|--------|-------|
| `as` | Assamese   | ✓      | ✓     |
| `bn` | Bengali    | ✓      | ✓     |
| `en` | English    |        | ✓     |
| `gu` | Gujarati   | ✓      | ✓     |
| `hi` | Hindi      | ✓      | ✓     |
| `kn` | Kannada    | ✓      | ✓     |
| `ml` | Malayalam  | ✓      | ✓     |
| `mr` | Marathi    | ✓      | ✓     |
| `ne` | Nepali     | ✓      | ✓     |
| `or` | Odia       | ✓      | ✓     |
| `pa` | Punjabi    | ✓      | ✓     |
| `sa` | Sanskrit   | ✓      | ✓     |
| `ta` | Tamil      | ✓      | ✓     |
| `te` | Telugu     | ✓      | ✓     |
| `ur` | Urdu       | ✓      | ✓     |

### Groups and Tasks

#### Groups

* `indicifeval_ground`: All 14 language tasks from the Ground config.
* `indicifeval_trans`: All 15 language tasks from the Trans config (includes English).

#### Tasks

* `indicifeval_ground_{lang}` — e.g., `indicifeval_ground_hi`
* `indicifeval_trans_{lang}` — e.g., `indicifeval_trans_hi`, `indicifeval_trans_en`

---

## Running the Task

### Prerequisites

```bash
pip install lm-eval
```

### Example Usage

**Run ground config — all 14 Indic languages:**

```bash
lm_eval --model hf \
    --model_args pretrained=sarvamai/sarvam-1 \
    --tasks indicifeval_ground \
    --batch_size auto \
    --output_path results/sarvam-1_indicifeval_ground
```

**Run trans config — all 15 languages (including English):**

```bash
lm_eval --model hf \
    --model_args pretrained=sarvamai/sarvam-1 \
    --tasks indicifeval_trans \
    --batch_size auto \
    --output_path results/sarvam-1_indicifeval_trans
```

**Run a single language (Hindi, ground):**

```bash
lm_eval --model hf \
    --model_args pretrained=sarvamai/sarvam-1 \
    --tasks indicifeval_ground_hi \
    --batch_size auto \
    --output_path results/sarvam-1_indicifeval_ground_hi
```

**Compare Indic vs English instruction-following (trans config):**

```bash
lm_eval --model hf \
    --model_args pretrained=sarvamai/sarvam-1 \
    --tasks indicifeval_trans_en,indicifeval_trans_hi,indicifeval_trans_bn \
    --batch_size auto \
    --output_path results/sarvam-1_indicifeval_trans_compare
```

---

### Notes

- **Always zero-shot** (`num_fewshot: 0` is hardcoded) — IFEval-style tasks are not designed for few-shot prompting.
- The dataset organises each language as a separate **split** (e.g., `split="hi"`), not a separate HuggingFace config. The `dataset_name` selects the config (`indicifeval-ground` or `indicifeval-trans`) and `test_split` selects the language split.
- **Instruction checking reuses the original IFEval infrastructure** (`lm_eval.tasks.ifeval.instructions_registry`). All constraint IDs in IndicIFEval match those in the English IFEval, so no additional language-specific checking code is required.
- Metrics (all higher is better):
  - `prompt_level_strict_acc`: fraction of prompts where **all** constraints are satisfied
  - `inst_level_strict_acc`: fraction of individual constraints satisfied
  - `prompt_level_loose_acc`: strict acc with minor formatting leniency (strips leading/trailing lines, removes `*`)
  - `inst_level_loose_acc`: loose version of instruction-level accuracy
- `max_gen_toks: 1280` matches the original IFEval setting.
