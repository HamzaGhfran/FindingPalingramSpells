"""code to remove single character from dictionary instead A and I because A and I counta as a word in dict"""
import loaddictionary

word_list  = loaddictionary.load("worddictionary1.txt")
word_list_clean = []
permissible = ('a','i')
for word in word_list:
    if len(word) > 1:
        word_list_clean.append(word)
    elif len(word) == 1 and word in permissible:
        word_list_clean.append(word)
    else:
        continue
print(word_list_clean)