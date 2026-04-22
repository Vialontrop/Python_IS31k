import csv

with open("data.csv", "r") as f, open("result.csv", "w", newline="") as out:
    reader = csv.DictReader(f)
    writer = csv.DictWriter(out, fieldnames=["name", "age"])

    writer.writeheader()

    for row in reader:
        if int(row["age"]) > 25:
            writer.writerow(row)
