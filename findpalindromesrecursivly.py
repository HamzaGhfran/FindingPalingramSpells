"""code to find palindrom letter with help of recursion"""
import sys

def recupalindrome(word):
    """function to check palindrome"""
    if len(word) <= 1:
        return "palindrome"
    if word[0] == word[-1]:
        return recupalindrome(word[1:-1])
    return "Not palindrome"

while True:
    text = input("\nEnter string to check weather palindrome or not : ")
    result = recupalindrome(text)
    print(result)
    try_again = input("\n\nPress Enter for more word or n to terminate!")
    if try_again == "n":
        sys.exit()
    else:
        continue
