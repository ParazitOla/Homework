### Task 7.1 Implement class-based context manager for opening and working with file, including handling exceptions.
# Do not use 'with open()'. Pass filename and mode via constructor.

class Context_Man:

    def __init__(self, file_name, method):
        try:
            self.file_obj = open(file_name, method)
        except Exception:
            print('Error open file')
            raise

    def __enter__(self):
        print('Context in...')
        return self.file_obj

    def __exit__(self, type, value, traceback):
        print('Context out...')
        self.file_obj.close()


if __name__ == "__main__":
    with Context_Man('f.txt', 'w') as f:
        f.write('hello')
