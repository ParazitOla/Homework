### Task 1.5
# Write a Python program to sort a dictionary by key.

my_dict = {'сто': 100, 'девяносто': 90, 'двенадцать': 12, 'пять': 5}
my_dict1 = {}
for k, v in sorted(my_dict.items()):
    # print(k, v)
    my_dict1[k] = v
print(my_dict1)
