# IndicQA

### Paper

Title: `IndicQA: A Multilingual Benchmark to Evaluate Question Answering capability of LLMs for Indic Languages`

IndicQA is a manually curated cloze-style reading comprehension benchmark for 11 Indic languages. Each instance consists of a context passage, a question, and one or more answer spans extracted from the context. Evaluation uses Exact Match (EM) and token-level F1 score, consistent with SQuAD-style extractive QA.

Dataset: https://huggingface.co/datasets/ai4bharat/IndicQA

### Supported Languages

| Code | Language   |
|------|------------|
| `as` | Assamese   |
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
@inproceedings{doddapaneni-etal-2023-towards,
    title = "Towards Leaving No {I}ndic Language Behind: Building Monolingual Corpora, Benchmark and Models for {I}ndic Languages",
    author = "Doddapaneni, Sumanth and Aralikatte, Rahul and Ramesh, Gowtham and Goyal, Shreya and Khapra, Mitesh M. and Kunchukuttan, Anoop and Kumar, Pratyush",
    booktitle = "Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    year = "2023",
    publisher = "Association for Computational Linguistics",
}
```

### Groups and Tasks

#### Groups

* `indicqa`: All 11 language tasks aggregated (weighted mean by size).

#### Tasks

* `indicqa_as`: Assamese
* `indicqa_bn`: Bengali
* `indicqa_gu`: Gujarati
* `indicqa_hi`: Hindi
* `indicqa_kn`: Kannada
* `indicqa_ml`: Malayalam
* `indicqa_mr`: Marathi
* `indicqa_or`: Odia
* `indicqa_pa`: Punjabi
* `indicqa_ta`: Tamil
* `indicqa_te`: Telugu

### Running the Task

**Run all Indic languages (group):**

```bash
lm_eval --model hf \
    --model_args pretrained=<model_name_or_path> \
    --tasks indicqa \
    --batch_size auto \
    --output_path results/indicqa
```

**Run a single language (e.g., Hindi):**

```bash
lm_eval --model hf \
    --model_args pretrained=<model_name_or_path> \
    --tasks indicqa_hi \
    --batch_size auto \
    --output_path results/indicqa_hi
```

**Run with a vLLM backend:**

```bash
lm_eval --model vllm \
    --model_args pretrained=<model_name_or_path>,dtype=bfloat16 \
    --tasks indicqa \
    --batch_size auto \
    --output_path results/indicqa
```

### Notes

- Only the `test` split is available; few-shot evaluation is not supported from the dataset itself.
- Output type is `generate_until` (open-ended generation stopped at newline).
- Metrics reported: `exact_match` and `f1` (mean, higher is better).
- EM and F1 are computed against all gold answers; the maximum score across answers is taken (standard SQuAD-style evaluation).
- Each language uses native-script labels for Context, Question, and Answer in the prompt.
