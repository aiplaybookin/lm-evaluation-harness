import transformers.data.metrics.squad_metrics as squad_metrics


LANGUAGES = {
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


def process_results_qa(doc, results):
    pred = results[0].strip()
    gold_answers = doc["answers"]["text"] if doc["answers"]["text"] else [""]
    em = max(squad_metrics.compute_exact(ans, pred) for ans in gold_answers)
    f1 = max(squad_metrics.compute_f1(ans, pred) for ans in gold_answers)
    return {"exact_match": em, "f1": f1}
