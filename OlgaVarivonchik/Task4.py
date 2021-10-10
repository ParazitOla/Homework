def split_by_index(s: str, indexes):
    # Task 4.4 Implement a function `split_by_index(s: str, indexes: List[int]) -> List[str]`
    # which splits the `s` string by indexes specified in `indexes`. Wrong indexes must be ignored.
    result = []
    curr_idx = 0
    for idx in indexes:
        if idx > len(s):
            break
        word = (s[curr_idx:idx])
        result.append(word)

        curr_idx = idx
    if curr_idx < len(s):
        word1 = (s[curr_idx:len(s)])
        result.append(word1)
    return result


if __name__ == '__main__':
    s1 = ("pythoniscool,isn'tit?")
    indexes1 = [6, 8, 12, 13, 18]
    print(split_by_index(s1, indexes1))
