def like_split(phrase):
    ### Task 4.3 Implement a function which works the same as `str.split` method (without using `str.split`)
    result = []
    word = ''
    for symbol in phrase:
        word += symbol
        result.append(word)
        word = ''
    return result


if __name__ == '__main__':
    phrase = ("twoteetoroomtwotwo")
    print(like_split(phrase))
