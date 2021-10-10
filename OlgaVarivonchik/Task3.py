### Task 5.3 File `data/students.csv` stores information about students in [CSV] format.
# This file contains the student’s names, age and average mark.
# 1) Implement a function which receives file path and returns names of top performer students
import csv
import operator


def get_top_performers(file_path, number_of_top_students=5):
    res = []
    with open(file_path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            res.append(row)

    resalt = []
    max_mark = sorted(res, key=operator.itemgetter('average mark'), reverse=True)[:number_of_top_students]
    for el in max_mark:
        resalt.append(el['student name'])
    print(resalt)

    return get_top_performers


# 2) Implement a function which receives the file path with students info and writes CSV student information
# to the new file in descending order of age.


def sort_by_age_csv(file_path):
    res = []
    with open(file_path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            res.append(row)

    sort_by_age = sorted(res, key=operator.itemgetter('age'), reverse=True)

    with open('sortbyage.csv', 'w', newline='') as file:
        columns = ['student name', 'age', 'average mark']
        writer = csv.DictWriter(file, delimiter=',', fieldnames=columns)
        writer.writeheader()
        for elem in sort_by_age:
            writer.writerow(elem)

    return


if __name__ == '__main__':
    get_top_performers('../data/students.csv', 5)

    sort_by_age_csv('../data/students.csv')
