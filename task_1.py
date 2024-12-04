import json
import time
import yaml


def yaml_to_json_1(yaml_file, json_file):
    with open(yaml_file, 'r', encoding='utf8') as yaml_in, open(json_file, "w", encoding='utf8') as json_out:
        yaml_object = yaml.safe_load(yaml_in)
        json.dump(yaml_object, json_out)


yaml_file = "input.yml"
json_file = "output_1.json"

yaml_to_json_1(yaml_file, json_file)
