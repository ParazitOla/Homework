def square_of_number(kwargs):
    # Task 4.10 Implement a function that takes a number as an argument and returns a dictionary, where the key is
    # a number and the value is the square of that number.
    d = {i: i ** 2 for i in range(1, kwargs + 1)}
    return d


if __name__ == '__main__':
    a = 5
    print(square_of_number(a))
