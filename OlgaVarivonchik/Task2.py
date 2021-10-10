def check_palindrome(word: str) -> str:
    # Task 4.2 Write a function that check whether a string is a palindrome or not.
    # Usage of any reversing functions is prohibited.
    x = 0
    y = len(word) - 1
    while x < y:
        if word[x] != word[y]:
            return False
        x = x + 1
        y = y - 1
    return True


if __name__ == '__main__':
    word = ('madam')
    if check_palindrome(word):
       print("Palindrome")
    else:
       print("Not palindrome")