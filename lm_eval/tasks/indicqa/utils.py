import transformers.data.metrics.squad_metrics as squad_metrics


def process_results_qa(doc, results):
    pred = results[0].strip()
    gold_answers = doc["answers"]["text"]
    if not gold_answers:
        gold_answers = [""]
    em = max(squad_metrics.compute_exact(ans, pred) for ans in gold_answers)
    f1 = max(squad_metrics.compute_f1(ans, pred) for ans in gold_answers)
    return {"exact_match": em, "f1": f1}
