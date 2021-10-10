### Task 1.6  Write a Python program to print all unique values of all dictionaries in a list.
list_dict = [{"V": "S001", "X": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},
             {"VIII": "S007"}]
my_list = []
v = 0
for val in list_dict:
    for v in val.values():
        my_list.append(v)
my_set = set(my_list)
print(my_set)
