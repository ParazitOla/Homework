### Task 5.2 Implement a function which search for most common words in the file.
# Use `data/lorem_ipsum.txt` file as a example.

import operator


def most_common_words(filepath, number_of_words):
    res = []
    with open(filepath, 'r') as f:
        text = f.readlines()

    for elem in text:
        elem = elem.rstrip('\n')
        elem = elem.upper()
        lst = elem.split(' ')

        for wrd in lst:
            s = wrd.rstrip('.')
            s = s.rstrip(',')
            if s != '':
                res.append(s)

    dict_tmp = {}
    dict_tmp = dict_tmp.fromkeys(res, 0)

    for elem in res:
        v = dict_tmp.get(elem) + 1
        k = elem
        dict_tmp[k] = v

    newa = list(dict(sorted(dict_tmp.items(), key=operator.itemgetter(1), reverse=True)[:number_of_words]).keys())

    return newa


if __name__ == '__main__':
    print(most_common_words('../data/lorem_ipsum.txt', 3))
