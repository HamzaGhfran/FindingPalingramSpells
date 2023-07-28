"""Finding Palindrom words from dictionary"""
import loaddictionary as ld
word_list = ld.load("word1.txt")
palindrom_list = []
for word in word_list:
    if len(word) > 1 and word[:] == word[::-1]:
        palindrom_list.append(word)
print("\nNumber of palindromes found = ", len(palindrom_list))
print(*palindrom_list, sep='\n')