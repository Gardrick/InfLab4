import json
import yaml


def yaml_to_json_1(yaml_file, json_file):
    with open(yaml_file, 'r', encoding='utf8') as yaml_in:
        yaml_object = yaml.safe_load(yaml_in)
    with open(json_file, "w", encoding='utf8') as json_out:
        json.dump(yaml_object, json_out, ensure_ascii=False, indent=4)


yaml_file = "input.yml"
json_file = "output_1.json"

yaml_to_json_1(yaml_file, json_file)
