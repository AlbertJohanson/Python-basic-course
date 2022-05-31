def palindrome(word):
    word = word.replace(" ", "")
    word = word.lower()
    reversed_word = word[::-1]


    if reversed_word == word:
        return True
    else:
        return False

    



def run():
    word = input("Enter a word: ");
    is_palindrome = palindrome(word)

    if is_palindrome == True:
        print("The word is a palindrome")
    else:
        print("The word is not a palindrome")


if __name__ == '__main__':
    run()