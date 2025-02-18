def single_root_words(root_word, *other_words):
    same_words = []
    m = root_word.lower()
    for i in range(len(other_words)):
        k = other_words[i]
        n = k.lower()
        if n in m or m in n:
            same_words.append(k)

    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)