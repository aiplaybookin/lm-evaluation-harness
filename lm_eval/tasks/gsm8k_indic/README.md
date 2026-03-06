# GSM8K-Indic

### Paper

GSM8K-Indic is a multilingual version of the GSM8K grade-school math benchmark, with problems translated into 10 Indic languages (plus English), each available in both native script and romanized form — 21 configurations in total.

Dataset: https://huggingface.co/datasets/sarvamai/gsm8k-indic

### Supported Configurations

| Config | Language | Script |
|---|---|---|
| `en` | English | Latin |
| `bn` | Bengali | Native |
| `bn_roman` | Bengali | Romanized |
| `gu` | Gujarati | Native |
| `gu_roman` | Gujarati | Romanized |
| `hi` | Hindi | Native |
| `hi_roman` | Hindi | Romanized |
| `kn` | Kannada | Native |
| `kn_roman` | Kannada | Romanized |
| `ml` | Malayalam | Native |
| `ml_roman` | Malayalam | Romanized |
| `mr` | Marathi | Native |
| `mr_roman` | Marathi | Romanized |
| `or` | Odia | Native |
| `or_roman` | Odia | Romanized |
| `pa` | Punjabi | Native |
| `pa_roman` | Punjabi | Romanized |
| `ta` | Tamil | Native |
| `ta_roman` | Tamil | Romanized |
| `te` | Telugu | Native |
| `te_roman` | Telugu | Romanized |

### Citation

```
@article{cobbe2021gsm8k,
  title={Training Verifiers to Solve Math Word Problems},
  author={Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},
  journal={arXiv preprint arXiv:2110.14168},
  year={2021}
}
```

### Groups and Tasks

#### Groups

* `gsm8k_indic`: All 21 configurations aggregated (weighted mean by size).

#### Tasks

* `gsm8k_indic_en`, `gsm8k_indic_bn`, `gsm8k_indic_bn_roman`, `gsm8k_indic_gu`, `gsm8k_indic_gu_roman`, `gsm8k_indic_hi`, `gsm8k_indic_hi_roman`, `gsm8k_indic_kn`, `gsm8k_indic_kn_roman`, `gsm8k_indic_ml`, `gsm8k_indic_ml_roman`, `gsm8k_indic_mr`, `gsm8k_indic_mr_roman`, `gsm8k_indic_or`, `gsm8k_indic_or_roman`, `gsm8k_indic_pa`, `gsm8k_indic_pa_roman`, `gsm8k_indic_ta`, `gsm8k_indic_ta_roman`, `gsm8k_indic_te`, `gsm8k_indic_te_roman`

### Running the Task

**Run all configurations (group):**

```bash
lm_eval --model hf \
    --model_args pretrained=<model_name_or_path> \
    --tasks gsm8k_indic \
    --batch_size auto \
    --output_path results/gsm8k_indic
```

**Run a single language (e.g., Hindi):**

```bash
lm_eval --model hf \
    --model_args pretrained=<model_name_or_path> \
    --tasks gsm8k_indic_hi \
    --batch_size auto \
    --output_path results/gsm8k_indic_hi
```

**Run with a vLLM backend:**

```bash
lm_eval --model vllm \
    --model_args pretrained=<model_name_or_path>,dtype=bfloat16 \
    --tasks gsm8k_indic \
    --batch_size auto \
    --output_path results/gsm8k_indic
```

### Notes

- Only the `test` split is available; zero-shot evaluation is used by default.
- Answers follow the GSM8K `#### {number}` format — the same filters and metric as the original GSM8K task are applied.
- Two filters are reported:
  - `strict-match`: extracts the number after `####`
  - `flexible-extract`: extracts the last number in the generation
- Metric: `exact_match` (mean, higher is better).
