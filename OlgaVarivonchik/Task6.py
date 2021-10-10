def get_shortest_word(s: str) -> str:
    # Implement a function `get_shortest_word(s: str) -> str` which returns the longest word in the given string.
    # The word can contain any symbols except whitespaces (` `, `\n`, `\t` and so on). If there are multiple
    # longest words in the string with a same length return the word that occures first.

    phr = phrase.split(' ')
    max_word = []
    result = ''
    for word in phr:
        max_word.append(len(word))
        result = phr[max_word.index(max(max_word))]
    return result


if __name__ == '__main__':
    phrase = ('Any pythonista like namespaces a lot')
    print(get_shortest_word(phrase))
