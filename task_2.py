import re
import time


def yaml_to_json_2(input_file, out_f):
    with open(input_file, 'r', encoding='utf8') as in_file:
        data = in_file.readlines()

    day_pattern = r'Среда:\n'
    day_repl = r'{\n"Среда":\n'

    lst = [
        "Среда:\n", " Расписание:\n", "  Пара1:\n", "  Пара2:\n", "  Пара3:\n", "  Пара4:\n", "  Пара5:\n",
        "  Пара6:\n", "  Пара7:\n", "  Пара8:\n"
    ]

    with open(out_f, 'w', encoding='utf8') as out_f:
        for i in range(len(data)):
            if data[i] in ["Среда:\n"]:
                rpl = re.sub(day_pattern, day_repl, data[i])
                out_f.write(rpl)

            elif data[i] in [" Расписание:\n"]:
                rpl = re.sub(" Расписание:\n", '\t{\n\t"Расписание":\n\t\t{\n', data[i])
                out_f.write(rpl)

            elif data[i] in ["  Пара1:\n", "  Пара2:\n", "  Пара3:\n", "  Пара4:\n", "  Пара5:\n", "  Пара6:\n",
                             "  Пара7:\n", "  Пара8:\n"]:
                sup_string = data[i].lstrip().split(':', maxsplit=1)
                out_f.write('\t\t"' + sup_string[0] + '":' + sup_string[1])
                out_f.write('\t\t\t{\n')

            else:
                if i + 1 == len(data):
                    sup_string = data[i].lstrip().split(':', maxsplit=1)
                    a = sup_string[1].split("\n")
                    out_f.write('\t\t\t\t"' + sup_string[0] + '":' + a[0].lstrip() + "\n")
                elif i + 1 != len(data) and (data[i + 1] in lst):
                    sup_string = data[i].lstrip().split(':', maxsplit=1)
                    a = sup_string[1].split("\n")
                    out_f.write('\t\t\t\t"' + sup_string[0] + '":' + a[0].lstrip() + "\n")
                else:
                    sup_string = data[i].lstrip().split(':', maxsplit=1)
                    a = sup_string[1].split("\n")
                    out_f.write('\t\t\t\t"' + sup_string[0] + '":' + a[0].lstrip() + ",\n")
                if i + 1 != len(data) and data[i + 1] in lst:
                    out_f.write('\t\t\t},\n')

        out_f.write("\t\t\t}\n\t\t}\n\t}\n}"'\n')


yaml_file = "input.yml"
json_file = "output_2.json"

yaml_to_json_2(yaml_file, json_file)
