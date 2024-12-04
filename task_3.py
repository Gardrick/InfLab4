import time


def count_spaces(row):
    return len(row) - len(row.lstrip())


def yaml_to_json(in_file, out_f):
    res = {}
    with open(in_file, 'r', encoding="utf8") as f:
        data = f.readlines()

    hierarchy = []

    for i in data:
        key, value = i.split(":", 1)
        layer, key = count_spaces(key) // 2, key.lstrip()
        hierarchy.insert(layer, key)

        while hierarchy[-1] != key:
            hierarchy.pop()
        if value == '\n':
            cur_tree = res
            for j in hierarchy:
                if j in cur_tree:
                    cur_tree = cur_tree[j]
                else:
                    cur_tree[j] = {}
        else:
            cur_tree = res
            for j in hierarchy:
                if j in cur_tree:
                    cur_tree = cur_tree[j]
                else:
                    cur_tree[j] = value.strip()

    a = str(res).replace('\'', '\"')
    with open(out_f, 'w', encoding='utf8') as out_f:
        out_f.write(a)


input_file = "input_3.yml"
#input_file = "input_3_alt.yml"
output_file = "output_3.yml"

start_time = time.time()

for i in range(100):
    yaml_to_json(input_file, output_file)

exit_time = time.time()
diff = exit_time - start_time
print("Время выполнения доп. задания 3 - ", str(diff))
