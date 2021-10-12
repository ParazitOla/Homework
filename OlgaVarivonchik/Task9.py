### Task 7.9 Implement an iterator class EvenRange, which accepts start and end of the interval as an init arguments
# and gives only even numbers during iteration.
# If user tries to iterate after it gave all possible numbers `Out of numbers!` should be printed.
# _Note: Do not use function `range()` at all_

class EvenRange:
    def __init__(self, start: int, stop: int):
        self.start = start
        self.stop = stop
        self.current = self.start

    def __iter__(self):
        return self

    def __next__(self):
        num = self.current
        if self.current < self.stop:
            if self.current % 2 == 0:
                self.current += 2
            else:
                num = self.current + 1
                self.current += 3
            return num
        else:
            print('Out of numbers!')
            raise StopIteration


class Iterator():

    def __iter__(self):
        return EvenRange()


er1 = EvenRange(5, 11)
print(next(er1))
print(next(er1))
print(next(er1))
print(next(er1))
print(next(er1))
print(next(er1))
#
# er2 = EvenRange(4, 5)
# for number in er2:
#     print(number)
