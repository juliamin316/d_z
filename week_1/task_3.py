def read_data(file_name):
    with open(file_name) as file:
        content = file.read()
    return content

def write_data(file_name, data):
    with open(file_name, "w") as f:
        f.write(data)

def format_text(text, symbols_q):
    lines = []
    words = text.split()
    current_line = words[0]
    for word in words[1:]:
        if len(current_line) + len(word) + 1 <= symbols_q:  # +1 для добавления пробела между словами
            current_line += " " + word
        else:
            lines.append(current_line)
            current_line = word
    lines.append(current_line)
    formatted_text = "\n".join(lines)
    return formatted_text

write_data('output.txt', format_text(read_data('input.txt'), 21))
