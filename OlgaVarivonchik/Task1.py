def replace_in_string(phrase: str) -> str:
    # Implement a function which receives a string and replaces all `"` symbols
    # with `'` and vise versa.
    new_phrase = ''
    for s in phrase:
        if s == "'":
            s = '"'
        elif s == '"':
            s = "'"
        new_phrase += s

    return new_phrase


if __name__ == '__main__':
    phrase = ("""This is an example: "containing 'nested' strings" """)
    print(replace_in_string(phrase))
