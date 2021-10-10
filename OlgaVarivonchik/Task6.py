### Task 5.6 Implement a decorator `call_once` which runs a function or method once and caches the result.
# All consecutive calls to this function should return cached result no matter the arguments.

from functools import wraps


def call_once(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not wrapper.called:
            wrapper.called = True
            return func(*args, **kwargs)
        print('уже все было')

    wrapper.called = False
    return wrapper


@call_once
def sum_of_numbers(a, b):
    return a + b


if __name__ == '__main__':
    print(sum_of_numbers(13, 42))
    print(sum_of_numbers(113, 421))
