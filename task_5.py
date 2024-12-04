def count_spaces(row):
    return len(row) - len(row.lstrip())


def yaml_to_dict(in_file):
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
    return res


def dict_to_tsv(data, filename):
    with open(filename, 'w', encoding='utf-16') as file:
        headers = ["День", "Время", "Предмет", "Тип", "Преподаватель", "Аудитория", "Корпус"]
        file.write('\t'.join(headers) + '\n')
        for day in data:
            for lesson in data[day]['Расписание']:
                file.write(f'{day}\t' + '\t'.join(data[day]['Расписание'][lesson][h] for h in headers[1:]) + '\n')


input_file = "input_3.yml"
data = yaml_to_dict(input_file)
dict_to_tsv(data, 'output_5.tsv')
