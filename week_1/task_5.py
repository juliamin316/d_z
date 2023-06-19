def find_anagrams(word_list):
    anagrams = {}
    for word in word_list:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]

    anagrams_list = []
    for key in sorted(anagrams.keys()):
        anagrams_list.append(sorted(anagrams[key]))

    return anagrams_list

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(find_anagrams(words))
