from task_main import yaml_to_json_main
from task_1 import yaml_to_json_1
from task_2 import yaml_to_json_2
from task_3 import yaml_to_dict
import time


def test(func, input, output):
    start_time = time.time()
    for i in range(100):
        func(input, output)
    return time.time() - start_time


print(
    f"Свой парсер: {test(yaml_to_json_main, 'input.yml', 'output.json')} секунд.",
    f"Парсер PyYAML + json: {test(yaml_to_json_1, 'input.yml', 'output_1.json')} секунд.",
    f"Свой парсер с регулярками: {test(yaml_to_json_2, 'input.yml', 'output_2.json')} секунд.",
    f"Свой парсер с форм. грамматиками: {test(yaml_to_dict, 'input.yml', 'output_3.yml')} секунд.",
    sep="\n"
)
