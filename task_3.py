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
                    current_tree[j] = value.strip()

    a = str(res).replace('\'', '\"')
    with open(output_file, 'w', encoding='utf8') as out:
        out.write(a)


input_file = "input_3.yml"
#input_file = "input_3_alt.yml"
output_file = "output_3.yml"

yaml_to_dict(input_file, output_file)
