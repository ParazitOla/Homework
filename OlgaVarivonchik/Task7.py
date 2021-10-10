def foo(list):
    ### Task 4.7 Implement a function `foo(List[int]) -> List[int]` which, given a list of integers,
    # return a new list such that each element at index `i` of the new list is the product of all the
    # numbers in the original array except the one at `i`.
    new_list = []
    for number in range(len(list_old)):
        list = list_old.copy()
        list.pop(number)
        a = 1
        for i in list:
            a *= i
        new_list.append(a)

    return new_list


if __name__ == '__main__':
    list_old = [3, 2, 1]
    print(foo(list_old))
