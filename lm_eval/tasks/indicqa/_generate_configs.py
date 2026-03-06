"""
Generate per-language YAML configs for ai4bharat/IndicQA.

Usage:
    python _generate_configs.py --base_yaml_path _default_template_yaml \
                                 --save_prefix_path indicqa
"""

import argparse
import logging
import os

import yaml


eval_logger = logging.getLogger(__name__)

# Language code -> (human-readable name, context label, question label, answer label)
LANGUAGES = {
    "as": ("Assamese", "প্ৰসংগ", "প্ৰশ্ন", "উত্তৰ"),
    "bn": ("Bengali", "প্রসঙ্গ", "প্রশ্ন", "উত্তর"),
    "gu": ("Gujarati", "સંદર્ભ", "પ્રશ્ન", "જવાબ"),
    "hi": ("Hindi", "प्रसंग", "सवाल", "उत्तर"),
    "kn": ("Kannada", "ಸಂದರ್ಭ", "ಪ್ರಶ್ನೆ", "ಉತ್ತರ"),
    "ml": ("Malayalam", "സന്ദർഭം", "ചോദ്യം", "ഉത്തരം"),
    "mr": ("Marathi", "संदर्भ", "प्रश्न", "उत्तर"),
    "or": ("Odia", "ପ୍ରସଙ୍ଗ", "ପ୍ରଶ୍ନ", "ଉତ୍ତର"),
    "pa": ("Punjabi", "ਸੰਦਰਭ", "ਸਵਾਲ", "ਜਵਾਬ"),
    "ta": ("Tamil", "சூழல்", "கேள்வி", "பதில்"),
    "te": ("Telugu", "సందర్భం", "ప్రశ్న", "సమాధానం"),
}


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base_yaml_path", required=True)
    parser.add_argument("--save_prefix_path", default="indicqa")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    base_yaml_name = os.path.split(args.base_yaml_path)[-1]

    for lang_code, (lang_name, ctx_label, q_label, a_label) in LANGUAGES.items():
        doc_to_text = f"{ctx_label}: {{{{context}}}}\n\n{q_label}: {{{{question}}}}\n\n{a_label}:"
        yaml_dict = {
            "include": base_yaml_name,
            "task": f"indicqa_{lang_code}",
            "dataset_name": f"indicqa.{lang_code}",
            "doc_to_text": doc_to_text,
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
