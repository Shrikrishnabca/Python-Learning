# Python has a built-in module called csv to work with CSV files.

# Writing to a CSV file
import csv

data = [
    ["name", "age", "city"],
    ["Krishan", 30, "Bangalore"],
    ["Ravi", 28, "Delhi"]
]


with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    for row in data:
        writer.writerow(row)


with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for line in reader:
        print(line)

with open("data.csv", mode="a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Nisha", 25, "Mumbai"])

# Writing with DictWriter
data = [
    {"name": "Krishan", "age": 30, "city": "Bangalore"},
    {"name": "Ravi", "age": 28, "city": "Delhi"}
]


with open("data.csv", mode="w", newline="") as file:
    fieldnames = ["name", "age", "city"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for line in reader:
        print(line)