"""
Generate per-language YAML configs for sarvamai/mmlu-indic.

Usage:
    python _generate_configs.py --base_yaml_path _default_template_yaml \
                                 --save_prefix_path mmlu_indic
"""

import argparse
import logging
import os

import yaml


eval_logger = logging.getLogger(__name__)

# Language code -> human-readable name
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
}


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base_yaml_path", required=True)
    parser.add_argument("--save_prefix_path", default="mmlu_indic")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    base_yaml_name = os.path.split(args.base_yaml_path)[-1]

    for lang_code, lang_name in LANGUAGES.items():
        yaml_dict = {
            "include": base_yaml_name,
            "task": f"mmlu_indic_{lang_code}",
            "dataset_name": lang_code,
            "description": f"Answer the following multiple-choice questions in {lang_name}.\n\n",
        }

        file_save_path = f"{args.save_prefix_path}_{lang_code}.yaml"
        eval_logger.info(f"Saving yaml for language {lang_code} to {file_save_path}")
        with open(file_save_path, "w", encoding="utf-8") as yaml_file:
            yaml.dump(
                yaml_dict,
                yaml_file,
                width=float("inf"),
                allow_unicode=True,
                default_style='"',
            )
        print(f"Wrote: {file_save_path}")
