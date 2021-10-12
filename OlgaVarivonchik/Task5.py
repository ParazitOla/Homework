### Task 7.5 Implement function for check that number is even and is greater than 2.
# Throw different exceptions for this errors.
# Custom exceptions must be derived from custom base exception(not Base Exception class).
class CustomBaseException(Exception):
    pass


class ExceptionNotEven(CustomBaseException):
    pass


class ExceptionLessTwo(CustomBaseException):
    pass


def check_num(arg: int):
    result = True
    try:
        if arg < 2:
            raise ExceptionLessTwo
        elif arg % 2 != 0:
            raise ExceptionNotEven
    except ExceptionNotEven:
        print('Number not even!')
        result = False
    except ExceptionLessTwo:
        print('Number less than 2')
        result = False;
    return result


if __name__ == '__main__':
    if not check_num(5):
        print('Error in source number!')
