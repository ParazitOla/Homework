### Task 7.2 Implement context manager for opening and working with file, including handling exceptions with
# @contextmanager decorator.

import contextlib


@contextlib.contextmanager
def file_hanlder(file_name, file_mode):
    file = open(file_name, file_mode)
    yield file
    file.close()


if __name__ == "__main__":
    with file_hanlder("test.txt", "w") as f:
        f.write("Test")
