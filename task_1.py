import json
import time
import yaml

yaml_file = "input.yml"
json_file = "output_1.json"

start_time = time.time()

for i in range(100):
    with open(yaml_file, 'r', encoding='utf8') as yaml_in, open(json_file, "w", encoding='utf8') as json_out:
        yaml_object = yaml.safe_load(yaml_in)
        json.dump(yaml_object, json_out)

exit_time = time.time()
diff = exit_time - start_time

print("Время выполнения, используя библиотеки - " + str(diff))
