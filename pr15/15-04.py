import csv

ages = []

with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        ages.append(int(row["age"]))

print(sum(ages) / len(ages))
