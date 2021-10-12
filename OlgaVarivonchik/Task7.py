# Implement your custom collection called MyNumberCollection. It should be able to contain only numbers. It should NOT inherit any other collections.
# 1. If user tries to add a string or any non numerical object there, exception `TypeError` should be raised.
# 2. Method init sholud be able to take either `start,end,step` arguments, where `start` - first number of collection,
# `end` - last number of collection or some ordered iterable collection (see the example).
# Implement following functionality:
# добавление нового элемента в конец коллекции
# объединение коллекций вместе с помощью `+`
# когда элемент адресуется по индексу (с использованием `[]`) пользователь должен получить квадрат адресуемого элемента
# при итерации с использованием цикла `for` элементы должны передаваться нормально
# пользователь должен иметь возможность распечатать всю коллекцию, как если бы она была списком

class MyNumberCollection:
    lst = []

    def __init__(self, start, end=None, step=None):
        if isinstance(start, (list, tuple)):
            if not all(isinstance(x, int) for x in start):
                raise TypeError(f"MyNumberCollection supports only numbers!")
            self.lst = list(start)
        elif all(isinstance(x, int) for x in (start, end, step)):
            for number in range(start, end, step):
                self.lst.append(number)
            if self.lst[-1] != end:
                self.lst.append(end)
        else:
            raise TypeError(f"MyNumberCollection supports only numbers!")

    def __repr__(self):
        return str(self.lst)

    def __add__(self, other):
        if isinstance(other, MyNumberCollection):
            return self.lst + other.lst
        else:
            raise TypeError(f"Incorrect operand!")

    def __radd__(self, other):
        return self.lst + other.lst

    def append(self, new_number):
        if isinstance(new_number, int):
            self.lst.append(new_number)
        else:
            raise TypeError(f"'{new_number}' - object is not a number!!")

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        self.index += 1
        if self.index < len(self.lst):
            return self.lst[self.index]
        else:
            raise StopIteration

    def __getitem__(self, idx):
        return self.lst[idx] ** 2


if __name__ == '__main__':
    col1 = MyNumberCollection(0, 5, 2)
    print(col1)
    #
    col2 = MyNumberCollection((1, 2, 3, 4, 5))
    print(col2)
    #
    # col3 = MyNumberCollection((1,2,3,"4", 5))
    #
    col1.append(7)
    print(col1)
    #
    # col2.append("string")
    #
    print(col1 + col2)
    #
    print(col1)
    #
    print(col2)
    #
    print(col2[4])
    #
    for item in col1:
        print(item)
