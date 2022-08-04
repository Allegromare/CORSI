import csv

with open("hogwarts.csv", "r") as file:
    reader = csv.reader(file)

    # Salta la prima riga del file csv (dove in genere vi sono le etichette dei campi)
    next(reader)

    # Effettua un ciclo per ogni riga 
    for row in reader:
        # Visualizza il primo campo della riga (row[0]), poi uno spazio, il trattino e un'altro spazio ed in seguito il secondo elemento della riga (row[1])
        print(f"{row[0]} - {row[1]}")


from cs50 import get_string

people = {
    "Carter": "+1-617-495-1000",
    "David": "+1-949-468-2750"
}

name = get_string("Name: ")
if name in people:
    number = people[name]
    print(f"Number: {number}")