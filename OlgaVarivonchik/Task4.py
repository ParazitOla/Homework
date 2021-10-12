### Task 7.4 Implement decorator for supressing exceptions. If exception not occure write log to console.
from contextlib import suppress


def decorator_f(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
            print('Exception not found')
        except Exception:
            print('Exception')

    return wrapper


@decorator_f
def test_f():
    print('Decorated function')
    raise ('Error')


if __name__ == '__main__':
    test_f()
