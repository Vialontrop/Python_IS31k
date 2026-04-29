# 18--12.py
with open("input.txt") as f1, open("filtered.txt","w") as f2:
    for line in f1:
        if len(line.strip()) > 5:
            f2.write(line)
