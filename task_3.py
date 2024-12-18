def count_spaces(row):
    return len(row) - len(row.lstrip())


def yaml_to_dict(input_file, output_file):
    res = {}
    with open(input_file, 'r', encoding="utf8") as f:
        data = f.readlines()

    hierarchy = []

    for i in data:
        key, value = i.split(":", 1)
        layer, key = count_spaces(key) // 2, key.lstrip()
        hierarchy.insert(layer, key)

        while hierarchy[-1] != key:
            hierarchy.pop()
        if value == '\n':
            current_tree = res
            for j in hierarchy:
                if j in current_tree:
                    current_tree = current_tree[j]
                else:
                    current_tree[j] = {}
        else:
            current_tree = res
            for j in hierarchy:
                if j in current_tree:
                    current_tree = current_tree[j]
                else:
                    if value.strip().startswith('['):
                        current_tree[j] = eval(value.strip())
                    elif value.strip().isnumeric():
                        current_tree[j] = float(value.strip())
                    else:
                        current_tree[j] = value.strip()

    a = str(res).replace('\'', '\"')
    with open(output_file, 'w', encoding='utf8') as out:
        out.write(a)
    return res


def dict_to_json_file(data, filename):
    def to_json_value(value, level):
        if isinstance(value, str):
            return f'"{value}"'
        elif isinstance(value, dict):
            return dict_to_json(value, level)
        elif isinstance(value, list):
            return list_to_json(value, level)
        elif isinstance(value, float) or isinstance(value, int):
            return f'{int(value)}' if value==int(value) else f'{value}'

    def dict_to_json(d, level):
        items = []
        for key, value in d.items():
            json_key = f'"{key}": '
            json_value = to_json_value(value, level + 1)
            items.append(f"{' ' * (level*4)}{json_key}{json_value}")
        return "{\n" + ",\n".join(items) + f"\n{' ' * ((level - 1)*4)}}}"

    def list_to_json(lst, level):
        items = [to_json_value(item, level + 1) for item in lst]
        return "[\n" + ",\n".join(f"{' ' * (level*4)}{item}" for item in items) + f"\n{' ' * ((level - 1)*4)}]"

    json_string = dict_to_json(data, 1)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json_string)


input_file = "input_3.yml"
output_file = "output_3.yml"

dictionary = yaml_to_dict(input_file, output_file)
dict_to_json_file(dictionary, 'output_3.json')
