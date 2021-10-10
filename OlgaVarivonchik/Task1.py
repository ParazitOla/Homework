### Task 5.1 Open file `data/unsorted_names.txt` in data folder. Sort the names and write them to a new file called
# `sorted_names.txt`. Each name should start with a new line as in the following example:

n = []
with open('../data/unsorted_names.txt', 'r') as f:
    text = f.readlines()
    for elem in text:
        elem = elem.rstrip('\n')
        n.append(elem)
n = sorted(n)

f1 = open('sorted_names.txt', 'w')
for index in n:
    f1.write(index + '\n')
f1.close()
