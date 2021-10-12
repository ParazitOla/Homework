### Task 7.3 Implement decorator with context manager support for writing execution time to log-file.
# See contextlib module.
import requests
from contextlib import contextmanager


@contextmanager
def context_manager():
    import time
    print('Enter method called')
    start = time.time()
    yield
    end = time.time()
    with open('log.txt', 'a') as f:
        f.write('Execution_Time={}\n'.format(end - start))


if __name__ == "__main__":
    with context_manager() as manager:
        webpage = requests.get('http://google.com')
        print('with statement block')
