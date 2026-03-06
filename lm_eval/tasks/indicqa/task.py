"""
IndicQA: Multilingual Extractive QA benchmark for Indic languages.
https://huggingface.co/datasets/ai4bharat/IndicQA

Loads data directly from the raw JSON files on HuggingFace to avoid the
deprecated dataset-script loader removed in datasets>=4.x.
"""

import json
import urllib.request
from statistics import mean

import datasets as hf_datasets
import transformers.data.metrics.squad_metrics as squad_metrics

from lm_eval.api.instance import Instance
from lm_eval.api.task import ConfigurableTask


_BASE_URL = "https://huggingface.co/datasets/ai4bharat/IndicQA/resolve/main/data/indicqa.{lang}.json"

# (context label, question label, answer label) in each language's script
_LANG_PROMPTS = {
    "as": ("প্ৰসংগ", "প্ৰশ্ন", "উত্তৰ"),
    "bn": ("প্রসঙ্গ", "প্রশ্ন", "উত্তর"),
    "gu": ("સંદર્ભ", "પ્રશ્ન", "જવાબ"),
    "hi": ("प्रसंग", "सवाल", "उत्तर"),
    "kn": ("ಸಂದರ್ಭ", "ಪ್ರಶ್ನೆ", "ಉತ್ತರ"),
    "ml": ("സന്ദർഭം", "ചോദ്യം", "ഉത്തരം"),
    "mr": ("संदर्भ", "प्रश्न", "उत्तर"),
    "or": ("ପ୍ରସଙ୍ଗ", "ପ୍ରଶ୍ନ", "ଉତ୍ତର"),
    "pa": ("ਸੰਦਰਭ", "ਸਵਾਲ", "ਜਵਾਬ"),
    "ta": ("சூழல்", "கேள்வி", "பதில்"),
    "te": ("సందర్భం", "ప్రశ్న", "సమాధానం"),
}


def _load_indicqa(lang: str) -> list[dict]:
    """Download and flatten SQuAD-format IndicQA JSON for a given language."""
    url = _BASE_URL.format(lang=lang)
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode("utf-8"))
    records = []
    for article in data["data"]:
        for para in article["paragraphs"]:
            context = para["context"]
            for qa in para["qas"]:
                records.append({
                    "id": qa["id"],
                    "context": context,
                    "question": qa["question"],
                    "answers": {
                        "text": [a["text"] for a in qa["answers"]],
                        "answer_start": [a["answer_start"] for a in qa["answers"]],
                    },
                })
    return records


class _IndicQABase(ConfigurableTask):
    """Base class for IndicQA language tasks. Subclass and set LANG."""

    LANG: str = None
    VERSION = 1
    OUTPUT_TYPE = "generate_until"

    def __init__(self, config=None):
        super().__init__(config={"metadata": {"version": self.VERSION}})

    def download(self, dataset_kwargs=None):
        records = _load_indicqa(self.LANG)
        self._hf_dataset = hf_datasets.Dataset.from_list(records)

    def has_training_docs(self):
        return False

    def has_validation_docs(self):
        return False

    def has_test_docs(self):
        return True

    def test_docs(self):
        return self._hf_dataset

    def doc_to_text(self, doc):
        ctx_label, q_label, a_label = _LANG_PROMPTS[self.LANG]
        return f"{ctx_label}: {doc['context']}\n\n{q_label}: {doc['question']}\n\n{a_label}:"

    def doc_to_target(self, doc):
        return " " + doc["answers"]["text"][0]

    def construct_requests(self, doc, ctx, chat_template=None, apply_chat_template=False, **kwargs):
        return [
            Instance(
                request_type="generate_until",
                doc=doc,
                arguments=(ctx, {"until": ["\n"], "do_sample": False, "temperature": 0.0}),
                idx=0,
                **kwargs,
            )
        ]

    def process_results(self, doc, results):
        pred = results[0].strip()
        gold_answers = doc["answers"]["text"] or [""]
        em = max(squad_metrics.compute_exact(ans, pred) for ans in gold_answers)
        f1 = max(squad_metrics.compute_f1(ans, pred) for ans in gold_answers)
        return {"exact_match": em, "f1": f1}

    def aggregation(self):
        return {"exact_match": mean, "f1": mean}

    def higher_is_better(self):
        return {"exact_match": True, "f1": True}


class IndicQA_as(_IndicQABase):
    LANG = "as"

class IndicQA_bn(_IndicQABase):
    LANG = "bn"

class IndicQA_gu(_IndicQABase):
    LANG = "gu"

class IndicQA_hi(_IndicQABase):
    LANG = "hi"

class IndicQA_kn(_IndicQABase):
    LANG = "kn"

class IndicQA_ml(_IndicQABase):
    LANG = "ml"

class IndicQA_mr(_IndicQABase):
    LANG = "mr"

class IndicQA_or(_IndicQABase):
    LANG = "or"

class IndicQA_pa(_IndicQABase):
    LANG = "pa"

class IndicQA_ta(_IndicQABase):
    LANG = "ta"

class IndicQA_te(_IndicQABase):
    LANG = "te"
