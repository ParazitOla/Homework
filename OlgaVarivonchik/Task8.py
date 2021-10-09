### Task 1.6
# Write a program which makes a pretty print of a part of the multiplication table.

a = 2
b = 4
c = 3
d = 7
my_list = [a, b, c, d]
my_list.sort()

for x in my_list:
    print(f'{x}\t', end='')
print('')
for x in (my_list):
    print(f'{x}\t', end='')
    for y in (my_list):
        print(f'{x * y}\t', end='')
    print('')
