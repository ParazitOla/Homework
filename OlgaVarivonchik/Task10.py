### Task 7.10 Implement a generator which will generate odd numbers endlessly.

def endless_generator():
    x = 1
    while True:
        yield x
        x += 2


gen = endless_generator()
while True:
    print(next(gen))