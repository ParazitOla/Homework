### Task 5.4 Look through file `modules/legb.py`.
# 1) Find a way to call `inner_function` without moving it from inside of `enclosed_function`.

a = "I am global variable!"


def enclosing_funcion1():
    a = "I am variable from enclosed function!"

    def inner_function():
        a = "I am local variable!"
        print(a)

    inner_function()


# 2.1) Modify ONE LINE in `inner_function` to make it print variable 'a' from global scope.

a = "I am global variable!"


def enclosing_funcion2():
    a = "I am variable from enclosed function!"

    def inner_function():
        global a
        a = a
        print(a)

    inner_function()


# 2.2) Modify ONE LINE in `inner_function` to make it print variable 'a' form enclosing function.

a = "I am global variable!"


def enclosing_funcion3():
    a = "I am variable from enclosed function!"

    def inner_function():
        # a = "I am local variable!"
        print(a)

    inner_function()


if __name__ == '__main__':
    enclosing_funcion1()
    enclosing_funcion2()
    enclosing_funcion3()
