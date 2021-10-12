### Task 7.11 Implement a generator which will geterate [Fibonacci numbers]
# (https://en.wikipedia.org/wiki/Fibonacci_number) endlessly.

def endless_fib_generator():
    a = 0
    b = 1
    print(a)
    print(b)
    while True:
        yield a + b
        v = b
        b += a
        a = v


gen = endless_fib_generator()
while True:
    print(next(gen))
