def single_root_words(root_word, *other_words):
    same_words = []
    for v in other_words:
        if root_word.lower() in v.lower() or v.lower() in root_word.lower():
            same_words.append(v)
    return same_words


print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))
