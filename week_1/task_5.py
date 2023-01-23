from collections import Counter
import re
# INPUT
with open('My_text.txt', 'r') as file:
    text = file.read()

# разделим текст на слова
words = text.split()

# создадим экземпляр Counter с помощью списка words
word_count = Counter(words)

# OUTPUT
top_10 = word_count.most_common(10)

# открытие файла для записи PROJECT
with open('My_text.txt', 'a') as file:
    for item in top_10:
