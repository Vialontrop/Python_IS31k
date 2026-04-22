count = 0

with open("input.txt", "r", encoding="utf-8") as f:
    for line in f:
        if line and line[0].isupper():
            count += 1

print(count)
