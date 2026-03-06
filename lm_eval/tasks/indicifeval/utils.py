# IndicIFEval uses the same instruction IDs and schema as the original English
# IFEval benchmark, so we reuse its instruction-checking infrastructure directly.
from lm_eval.tasks.ifeval.utils import (
    agg_inst_level_acc,
    process_results,
)


__all__ = ["process_results", "agg_inst_level_acc"]
