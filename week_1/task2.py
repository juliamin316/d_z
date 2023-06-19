def read_data(file_name):
    with open(file_name) as file:
        content = file.read()
    return content

def write_data(file_name, data):
    with open(file_name, "w") as f:
        f.write(data)

def format_text(text):
    first_s = text.splitlines()  # подготовка для сортировки
    v_list = []
    for file_names in first_s:
        value = file_names[file_names.index('KP2.2-') + len('KP2.2-'):file_names.index(' - ')]
        v_list.append(float(value))
    rows_v = list(zip(v_list, first_s))
    sorted_data = []
    for i in sorted(rows_v):
        sorted_data.append(str(i[1]) + '\n')

    return sorted_data

write_data('output.txt', format_text(read_data('input.txt')))
