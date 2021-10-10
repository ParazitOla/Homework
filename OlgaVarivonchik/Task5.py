### Task 5.5 Implement a decorator `remember_result` which remembers last result of function it decorates and
# prints it before next call.

def remember_result(func):
    a = None

    def wrapper(*args, **kwargs):
        nonlocal a
        print(f'Last result = ', a)
        a = func(*args, **kwargs)

    return wrapper


@remember_result
def sum_list(*args):
    result = ""
    for item in args:
        result += item
    print(f"Current result = '{result}'")
    return result


if __name__ == '__main__':
    sum_list("odffgh", "c1452")
    sum_list("2234sfgh", "dffd")
    sum_list("2234ssffgh", "dfsdfsffd")
