import pickle


# data = urlopen('https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt')
# words = []
# for raw_word in data:
#     string_word = str(raw_word)
#     string_word = string_word[2:len(string_word)-5]
#     words.append(string_word)
# words = sorted(words, key=len)
# words = words[2584:]
# words = words[::-1]
# print(words)
# with open('words.pickle', 'wb') as f:
#     pickle.dump(words, f)

def split_words(string):
    with open('words.pickle', 'rb') as f:
        words = pickle.load(f)
    for word in words:
        word_with_spaces = ' ' + word + ' '
        string = string.replace(word, word_with_spaces)
    return string
