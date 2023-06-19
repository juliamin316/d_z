def read_data(path):
    with open(path, encoding="utf8") as file:
        data = file.read()
    return data


def format_text(text):
    text = text.lower().replace('.', '').replace(',', '')
    words = text.split()
    words_count = {}
    for word in words:
        words_count[word] = words_count.get(word, 0) + 1
    sorted_words_count = sorted(words_count.items(), key=lambda x: [x[1], x[0]], reverse=True)
    top_words_count = sorted_words_count[:10]
    new_text = '\n'.join([f"{word},{count}" for word, count in top_words_count])
    return new_text


def write_data(path, data):
    with open(path, "w", encoding="utf8") as file:
        file.write(data)


write_data('output.txt', format_text(read_data('input.txt')))

