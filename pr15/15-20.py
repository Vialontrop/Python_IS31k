from collections import defaultdict

errors = defaultdict(int)

with open("log.txt", "r") as f:
    for line in f:
        if "ERROR" in line:
            date = line.split()[0]
            errors[date] += 1

for date, count in errors.items():
    print(f"{date}: {count}")
