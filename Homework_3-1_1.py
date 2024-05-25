def single_root_words(root_word, *other_words):     # str.count(sub[, start[, end]]), other_words - list
    same_words = []
    root_word_low = str(root_word).lower()
    for word in other_words:
        word_low = str(word).lower()
        if word_low.count(root_word_low) or  root_word_low.count(word_low):
            word_str = str(word)
            same_words.append(word_str)
    print(same_words)

single_root_words(True, 'Muca77tty', 'cat', 'buba', 7, 'kop', 112334567789, 'truegon', True, 'ru')
single_root_words(77, 'Muca77tty', 'cat', 'buba', 7, 'kop', 112334567789, 'truegon', True, 'ru')
single_root_words('Cat', 'Mucat77ty', 'cat', 'buba', 7, 'kop', 112334567789, 'truegon', True, 'ru')