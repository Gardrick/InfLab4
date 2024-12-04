import time


def yaml_to_json_main(input_file, output_file):
    with open(input_file, 'r', encoding='utf8') as in_file:
        data = in_file.readlines()
        numb_lines = len(data)

    out_file = open(output_file, 'w', encoding='utf8')
    out_file.write("{\n")

    lst = [
        "Среда:\n", " Расписание:\n", "  Пара1:\n", "  Пара2:\n", "  Пара3:\n", "  Пара4:\n", "  Пара5:\n",
        "  Пара6:\n", "  Пара7:\n", "  Пара8:\n"
    ]

    for line in range(0, numb_lines):
        if data[line] in ["Среда:\n"]:
            if data[0] == data[line]:
                sup_string = data[line].lstrip().split(':', maxsplit=1)
                out_file.write('"' + sup_string[0] + '":' + sup_string[1])
            else:
                sup_string = data[line].lstrip().split(':', maxsplit=1)
                out_file.write(' }\n }\n\n"' + sup_string[0] + '":' + sup_string[1])

        elif data[line] in [" Расписание:\n"]:
            sup_string = data[line].lstrip().split(':', maxsplit=1)
            out_file.write('\t{\n')
            out_file.write('\t"' + sup_string[0] + '":' + sup_string[1])
            out_file.write('\t\t{\n')

        elif data[line] in ["  Пара1:\n", "  Пара2:\n", "  Пара3:\n", "  Пара4:\n", "  Пара5:\n", "  Пара6:\n",
                            "  Пара7:\n", "  Пара8:\n"]:
            sup_string = data[line].lstrip().split(':', maxsplit=1)
            out_file.write('\t\t"' + sup_string[0] + '":' + sup_string[1])
            out_file.write('\t\t\t{\n')

        else:
            if line + 1 == numb_lines:
                sup_string = data[line].lstrip().split(':', maxsplit=1)
                a = sup_string[1].split("\n")
                out_file.write('\t\t\t\t"' + sup_string[0] + '":' + a[0].lstrip() + "\n")
            elif line + 1 != numb_lines and (data[line + 1] in lst):
                sup_string = data[line].lstrip().split(':', maxsplit=1)
                a = sup_string[1].split("\n")
                out_file.write('\t\t\t\t"' + sup_string[0] + '":' + a[0].lstrip() + "\n")
            else:
                sup_string = data[line].lstrip().split(':', maxsplit=1)
                a = sup_string[1].split("\n")
                out_file.write('\t\t\t\t"' + sup_string[0] + '":' + a[0].lstrip() + ",\n")
            if line + 1 != numb_lines and data[line + 1] in lst:
                out_file.write('\t\t\t},\n')

    out_file.write("\t\t\t}\n\t\t}\n\t}\n}"'\n')
    out_file.close()


yaml_file = "input.yml"
json_file = "output.json"

yaml_to_json_main(yaml_file, json_file)
