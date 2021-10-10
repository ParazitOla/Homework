import string


# Implement a bunch of functions which receive a changeable number of strings and return next parameters:
# 1) characters that appear in all strings
# 2) characters that appear in at least one string
# 3) characters that appear at least in two strings
# 4) characters of alphabet, that were not used in any string
# Note: use `string.ascii_lowercase` for list of alphabet letters

def test_1_1(strings):
    result = set(string.ascii_lowercase)
    for s in strings:
        result.intersection_update(set(s))
    return sorted(result)


def test_1_2(strings):
    result = set()
    for s in strings:
        result = result.union(set(s))
    return sorted(result)


def test_1_3(strings):
    result = set()
    for i in range(len(strings) - 1):
        set_r = set()
        for j in range(i + 1, len(strings)):
            set_r.update(set(strings[i]).intersection(set(strings[j])))
        result.update(set_r)
    return sorted(result)


def test_1_4(strings):
    tmp_set = test_1_2(strings)
    result = set(string.ascii_lowercase)
    result = result.difference(tmp_set)
    return sorted(result)


if __name__ == '__main__':
    # test_strings = ["hello friends", "world peace", "python very good", ]
    test_strings = ["hello", "world", "python", ]
    print(test_1_1(test_strings))
    print(test_1_2(test_strings))
    print(test_1_3(test_strings))
    print(test_1_4(test_strings))
