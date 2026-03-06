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

def _make_filter(lang, direction):
    def process_docs(dataset):
        return dataset.filter(
            lambda x: x["lang"] == lang and x["translation_direction"] == direction
        )
    return process_docs


# en → indic  (enxx)
process_docs_enxx_bn = _make_filter("bn", "enxx")
process_docs_enxx_gu = _make_filter("gu", "enxx")
process_docs_enxx_hi = _make_filter("hi", "enxx")
process_docs_enxx_kn = _make_filter("kn", "enxx")
process_docs_enxx_ml = _make_filter("ml", "enxx")
process_docs_enxx_mr = _make_filter("mr", "enxx")
process_docs_enxx_or = _make_filter("or", "enxx")
process_docs_enxx_pa = _make_filter("pa", "enxx")
process_docs_enxx_ta = _make_filter("ta", "enxx")
process_docs_enxx_te = _make_filter("te", "enxx")
process_docs_enxx_ur = _make_filter("ur", "enxx")

# indic → en  (xxen)
process_docs_xxen_bn = _make_filter("bn", "xxen")
process_docs_xxen_gu = _make_filter("gu", "xxen")
process_docs_xxen_hi = _make_filter("hi", "xxen")
process_docs_xxen_kn = _make_filter("kn", "xxen")
process_docs_xxen_ml = _make_filter("ml", "xxen")
process_docs_xxen_mr = _make_filter("mr", "xxen")
process_docs_xxen_or = _make_filter("or", "xxen")
process_docs_xxen_pa = _make_filter("pa", "xxen")
process_docs_xxen_ta = _make_filter("ta", "xxen")
process_docs_xxen_te = _make_filter("te", "xxen")
process_docs_xxen_ur = _make_filter("ur", "xxen")


# ── Metrics ───────────────────────────────────────────────────────────────────

def bleu(predictions, references):
    return (predictions[0], references[0])


def agg_bleu(items):
    bleu_fn = evaluate.load("bleu")
    predictions, references = zip(*items)
    return bleu_fn.compute(predictions=list(predictions), references=list(references))["bleu"]


def chrf(predictions, references):
    return (predictions[0], references[0])


def agg_chrf(items):
    chrf_fn = evaluate.load("chrf")
    predictions, references = zip(*items)
    return chrf_fn.compute(predictions=list(predictions), references=list(references))["score"]
