# Indic TriviaQA MCQ

### Paper

Title: `TriviaQA: A Large Scale Distantly Supervised Challenge Dataset for Reading Comprehension`
Abstract: https://arxiv.org/abs/1705.03551

TriviaQA is a reading comprehension dataset containing over 650K question-answer-evidence triples. This Indic variant (`sarvamai/trivia-qa-indic-mcq`) reformulates TriviaQA questions as multiple-choice questions (MCQ) across 11 Indic languages.

Dataset: https://huggingface.co/datasets/sarvamai/trivia-qa-indic-mcq

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
@InProceedings{JoshiTriviaQA2017,
    author = {Joshi, Mandar and Choi, Eunsol and Weld, Daniel S. and Zettlemoyer, Luke},
    title = {TriviaQA: A Large Scale Distantly Supervised Challenge Dataset for Reading Comprehension},
    booktitle = {Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics},
    month = {July},
    year = {2017},
    address = {Vancouver, Canada},
    publisher = {Association for Computational Linguistics},
}
```

### Groups and Tasks

#### Groups

* `indic_triviaqa_mcq`: All 11 language tasks aggregated (weighted mean by size).

#### Tasks

* `indic_triviaqa_mcq_bn`: Bengali
* `indic_triviaqa_mcq_en`: English
* `indic_triviaqa_mcq_gu`: Gujarati
* `indic_triviaqa_mcq_hi`: Hindi
* `indic_triviaqa_mcq_kn`: Kannada
* `indic_triviaqa_mcq_ml`: Malayalam
* `indic_triviaqa_mcq_mr`: Marathi
* `indic_triviaqa_mcq_or`: Odia
* `indic_triviaqa_mcq_pa`: Punjabi
* `indic_triviaqa_mcq_ta`: Tamil
* `indic_triviaqa_mcq_te`: Telugu

### Running the Task

**Run all Indic languages (group):**

```bash
lm_eval --model hf \
    --model_args pretrained=<model_name_or_path> \
    --tasks indic_triviaqa_mcq \
    --num_fewshot 5 \
    --batch_size auto \
    --output_path results/indic_triviaqa_mcq
```

**Run a single language (e.g., Hindi):**

```bash
lm_eval --model hf \
    --model_args pretrained=<model_name_or_path> \
    --tasks indic_triviaqa_mcq_hi \
    --num_fewshot 5 \
    --batch_size auto \
    --output_path results/indic_triviaqa_mcq_hi
```

**Run multiple specific languages:**

```bash
lm_eval --model hf \
    --model_args pretrained=<model_name_or_path> \
    --tasks indic_triviaqa_mcq_hi,indic_triviaqa_mcq_bn,indic_triviaqa_mcq_ta \
    --num_fewshot 5 \
    --batch_size auto \
    --output_path results/
```

**Run with a vLLM backend:**

```bash
lm_eval --model vllm \
    --model_args pretrained=<model_name_or_path>,dtype=bfloat16 \
    --tasks indic_triviaqa_mcq \
    --num_fewshot 5 \
    --batch_size auto \
    --output_path results/indic_triviaqa_mcq
```

### Notes

- Only the `validation` split is available; it is used for both evaluation and few-shot sampling.
- The task uses `multiple_choice` output type with 4 options (A/B/C/D).
- Metrics reported: `acc` and `acc_norm` (mean, higher is better).
- Few-shot examples are sampled using the `first_n` sampler from the validation split.
