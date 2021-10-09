### Task 1.2 Write a Python program to count the number of characters (character frequency) in a string
# (ignore case of letters).

word = input("Task 1.2. let's check how many characters in a string: ")
characters = list(word.upper())
found = dict.fromkeys(characters, 0)
for letter in characters:
    if letter in found:
        found[letter] += 1
print("Input:", word + '\n' + "Output:", str(found))
