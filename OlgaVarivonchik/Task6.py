### Task 7.6 Create console program for proving Goldbach's conjecture.
# Program accepts number for input and print result. For pressing 'q' program succesfully close.
# Use function from Task 5.5 for validating input, handle all exceptions and print user friendly output.
from Task5 import *


def simple(n):
    i = 2
    while (i < n):
        if n % i == 0:
            return False
        i += 1
    return True


def check_g(number):
    for i in range(2, number):
        if simple(i):
            if simple(number - i):
                print(number, '=', i, '+', number - i)
                return True
    return False


if __name__ == '__main__':
    st = input('Enter number:')
    while st != 'q':
        n = int(st)
        if check_num(n):
            check_g(n)
        st = input('Enter number:')
