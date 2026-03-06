"""
Generate per-language YAML configs for sarvamai/gsm8k-indic.

Usage:
    python _generate_configs.py --base_yaml_path _default_template_yaml \
                                 --save_prefix_path gsm8k_indic
"""

import argparse
import logging
import os

import yaml


eval_logger = logging.getLogger(__name__)

# dataset_name -> human-readable description suffix
CONFIGS = {
    "bn": "Bengali",
    "bn_roman": "Bengali (Romanized)",
    "en": "English",
    "gu": "Gujarati",
    "gu_roman": "Gujarati (Romanized)",
    "hi": "Hindi",
    "hi_roman": "Hindi (Romanized)",
    "kn": "Kannada",
    "kn_roman": "Kannada (Romanized)",
    "ml": "Malayalam",
    "ml_roman": "Malayalam (Romanized)",
    "mr": "Marathi",
    "mr_roman": "Marathi (Romanized)",
    "or": "Odia",
    "or_roman": "Odia (Romanized)",
    "pa": "Punjabi",
    "pa_roman": "Punjabi (Romanized)",
    "ta": "Tamil",
    "ta_roman": "Tamil (Romanized)",
    "te": "Telugu",
    "te_roman": "Telugu (Romanized)",
}


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base_yaml_path", required=True)
    parser.add_argument("--save_prefix_path", default="gsm8k_indic")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    base_yaml_name = os.path.split(args.base_yaml_path)[-1]

    for config_name, lang_name in CONFIGS.items():
        task_name = f"gsm8k_indic_{config_name}"
        yaml_dict = {
            "include": base_yaml_name,
            "task": task_name,
            "dataset_name": config_name,
        }

        file_save_path = f"{args.save_prefix_path}_{config_name}.yaml"
        eval_logger.info(f"Saving yaml for {config_name} to {file_save_path}")
        with open(file_save_path, "w", encoding="utf-8") as yaml_file:
            yaml.dump(
                yaml_dict,
                yaml_file,
                width=float("inf"),
                allow_unicode=True,
                default_style='"',
            )
        print(f"Wrote: {file_save_path}")
