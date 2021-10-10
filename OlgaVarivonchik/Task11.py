def combine_dicts(*args):
    # Implement a function, that receives changeable number of dictionaries(keys - letters, values - numbers) and
    # combines them into one dictionary. Dict values should be summarized in case of identical keys

    dict_result = {}
    for d in args:
        for k in d:
            v = d.get(k)
            if k in dict_result.keys():
                v += dict_result.get(k)
            dict_result.update(d.fromkeys(k, v))
    return dict_result


if __name__ == '__main__':
    dict_1 = {'a': 100, 'b': 200}
    dict_2 = {'a': 200, 'c': 300, 'd': 100}
    dict_3 = {'a': 600, 'd': 100}
    print(combine_dicts(dict_1, dict_2, dict_3))
