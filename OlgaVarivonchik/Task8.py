### Task 7.8 Implement your custom iterator class called MySquareIterator which gives squares of elements of
# collection it iterates through.

class SimpleIterator:
    lst = []
    def __init__(self, my_list):
        self.lst = my_list
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < len(self.lst):
            k = self.lst[self.current]
            self.current += 1
            return k**2
        else:
            raise StopIteration

class MySquareIterator():
    lst = []
    def __init__(self, my_list):
        self.lst = my_list

    def __iter__(self):
        return SimpleIterator(self.lst)

if __name__ == '__main__':
    s_lst = [1, 2, 3, 4, 5, 6]
    s_iter = MySquareIterator(s_lst)
    for i in s_iter:
        print(i)



