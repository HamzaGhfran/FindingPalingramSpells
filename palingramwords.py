"""code to find all palindrom string in word"""

import loaddictionary as ld

word_list = ld.load("worddictionary1.txt")
def palingram():
    palindrom_list = []
    for word in word_list:
        end = len(word)
        revers_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == revers_word[:end-i] and revers_word[end-i:] in word_list:
                    palindrom_list.append((word, revers_word[:end-i]))
                if word[:i] == revers_word[end-i:] and revers_word[:end-i] in word_list:
                    palindrom_list.append((revers_word[:end-i],word))
    return palindrom_list
palindrom = palingram()
print(palindrom)