#!/usr/bin/env bash
# -----------------------------------------------------------------------
# Run lm-evaluation-harness on sarvamai/trivia-qa-indic-mcq
#
# Usage:
#   bash scripts/run_indic_triviaqa_mcq.sh <model_name_or_path> [options]
#
# Examples:
#   # Evaluate all 11 languages at once (group task):
#   bash scripts/run_indic_triviaqa_mcq.sh "sarvamai/sarvam-2b-v0.5"
#
#   # Evaluate specific languages only:
#   bash scripts/run_indic_triviaqa_mcq.sh "sarvamai/sarvam-2b-v0.5" --lang hi,bn,ta
#
#   # Use a specific number of few-shot examples:
#   bash scripts/run_indic_triviaqa_mcq.sh "sarvamai/sarvam-2b-v0.5" --num_fewshot 5
#
#   # Evaluate an OpenAI-compatible API endpoint:
#   bash scripts/run_indic_triviaqa_mcq.sh "local-chat-completions" \
#       --model_args "base_url=http://localhost:8000/v1,model=my-model"
# -----------------------------------------------------------------------

set -euo pipefail

MODEL="${1:-}"
if [[ -z "$MODEL" ]]; then
    echo "Error: MODEL argument is required."
    echo "Usage: $0 <model_name_or_path> [--lang LANG_CODES] [--num_fewshot N] [--model_args ARGS]"
    exit 1
fi
shift

# ---- Defaults -----------------------------------------------------------
LANGS=""            # empty = run full group (all 11 languages)
NUM_FEWSHOT=0
BATCH_SIZE="auto"
OUTPUT_DIR="results/indic_triviaqa_mcq"
MODEL_TYPE="hf"     # "hf" | "vllm" | "local-chat-completions"
MODEL_ARGS=""
EXTRA_ARGS=""

# ---- Parse optional flags -----------------------------------------------
while [[ $# -gt 0 ]]; do
    case "$1" in
        --lang)         LANGS="$2";         shift 2 ;;
        --num_fewshot)  NUM_FEWSHOT="$2";   shift 2 ;;
        --batch_size)   BATCH_SIZE="$2";    shift 2 ;;
        --output_dir)   OUTPUT_DIR="$2";    shift 2 ;;
        --model_type)   MODEL_TYPE="$2";    shift 2 ;;
        --model_args)   MODEL_ARGS="$2";    shift 2 ;;
        *)              EXTRA_ARGS="$EXTRA_ARGS $1"; shift ;;
    esac
done

# ---- Build task list ----------------------------------------------------
if [[ -z "$LANGS" ]]; then
    # Run the full group (all 11 languages)
    TASKS="indic_triviaqa_mcq"
else
    # Build comma-separated individual task names, e.g. hi,bn -> indic_triviaqa_mcq_hi,indic_triviaqa_mcq_bn
    TASKS=""
    IFS=',' read -ra LANG_ARRAY <<< "$LANGS"
    for lang in "${LANG_ARRAY[@]}"; do
        TASKS="${TASKS:+$TASKS,}indic_triviaqa_mcq_${lang}"
    done
fi

# ---- Build model args ---------------------------------------------------
BASE_MODEL_ARGS="pretrained=${MODEL}"
if [[ -n "$MODEL_ARGS" ]]; then
    BASE_MODEL_ARGS="${BASE_MODEL_ARGS},${MODEL_ARGS}"
fi

# ---- Run evaluation -----------------------------------------------------
mkdir -p "$OUTPUT_DIR"

echo "=============================================="
echo " Indic TriviaQA MCQ Benchmark"
echo "=============================================="
echo " Model:       $MODEL"
echo " Model type:  $MODEL_TYPE"
echo " Tasks:       $TASKS"
echo " Few-shot:    $NUM_FEWSHOT"
echo " Batch size:  $BATCH_SIZE"
echo " Output dir:  $OUTPUT_DIR"
echo "=============================================="

python -m lm_eval \
    --model "$MODEL_TYPE" \
    --model_args "$BASE_MODEL_ARGS" \
    --tasks "$TASKS" \
    --include_path lm_eval/tasks/indic_triviaqa_mcq \
    --num_fewshot "$NUM_FEWSHOT" \
    --batch_size "$BATCH_SIZE" \
    --output_path "$OUTPUT_DIR" \
    --log_samples \
    $EXTRA_ARGS

echo ""
echo "Results saved to: $OUTPUT_DIR"
