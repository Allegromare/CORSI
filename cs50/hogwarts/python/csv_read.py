import csv

file = open("phonebook.csv", "r")

reader = csv.reader(file)

for row in reader:
    print(row[0], row[1])

file.close()
