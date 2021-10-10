### Task 1.7
# Write a Python program to convert a given tuple of positive integers into an integer.

my_tuple = (1, 52, 358, 4,)
s = ''
for number in my_tuple:
    s += str(number)
print(int(s))
