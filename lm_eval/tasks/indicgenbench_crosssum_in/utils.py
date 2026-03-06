import evaluate


LANGUAGE_NAMES = {
    "bn": "Bengali",
    "gu": "Gujarati",
    "hi": "Hindi",
    "kn": "Kannada",
    "ml": "Malayalam",
    "mr": "Marathi",
    "or": "Odia",
    "pa": "Punjabi",
    "ta": "Tamil",
    "te": "Telugu",
    "ur": "Urdu",
}


# ── Language filters ──────────────────────────────────────────────────────────

def _make_lang_filter(lang):
    def process_docs(dataset):
        return dataset.filter(lambda x: x["lang"] == lang)
    return process_docs


process_docs_bn = _make_lang_filter("bn")
process_docs_gu = _make_lang_filter("gu")
process_docs_hi = _make_lang_filter("hi")
process_docs_kn = _make_lang_filter("kn")
process_docs_ml = _make_lang_filter("ml")
process_docs_mr = _make_lang_filter("mr")
process_docs_or = _make_lang_filter("or")
process_docs_pa = _make_lang_filter("pa")
process_docs_ta = _make_lang_filter("ta")
process_docs_te = _make_lang_filter("te")
process_docs_ur = _make_lang_filter("ur")


# ── Metrics ───────────────────────────────────────────────────────────────────

def rouge_l(predictions, references):
    return (predictions[0], references[0])


def agg_rouge_l(items):
    rouge = evaluate.load("rouge")
    predictions, references = zip(*items)
    return rouge.compute(predictions=list(predictions), references=list(references))["rougeL"]
