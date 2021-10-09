### Task 1.4 Create a program that asks the user for a number and then prints out a list of all the [divisors]
# (https://en.wikipedia.org/wiki/Divisor) of that number.

number = int(input("Task 1.3. Divisos of: "))
print(number)
mylist = []
for element in range(0 + 1, (number + 1)):
    if number % element == 0:
        divide = int(number / element)
        mylist.append(element)
print(mylist)
