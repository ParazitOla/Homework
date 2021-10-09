### Task 1.3 Write a Python program that accepts a comma separated sequence of words as input and prints
# the unique words in sorted form.

word = input("Task 1.3. let's do unique: ")
word_in_list = word.split(sep=',')
unique = list(set(word_in_list))
unique.sort()
print(unique)
