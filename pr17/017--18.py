import csv
with open('users.csv') as f:
    reader=csv.reader(f)
    for r in reader:
        print(r)