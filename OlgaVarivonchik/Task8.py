def get_pairs(lst):
    ### Task 4.8 Implement a function `get_pairs(lst: List) -> List[Tuple]` which returns a list of tuples
    # containing pairs of elements. Pairs should be formed as in the example. If there is only one element
    # in the list return `None` instead.
    result = []
    if len(lst) in (0, 1):
        return None
    else:
        for v in range(len(lst) - 1):
            k = []
            k.append(lst[v])
            k.append(lst[v + 1])
            result.append(tuple(k))
    return result


if __name__ == '__main__':
    lis = ['need', 'to', 'sleep', 'more']
    print(get_pairs(lis))
