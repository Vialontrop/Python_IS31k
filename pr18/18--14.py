# 18--14.py
with open("input.txt") as f1, open("no_empty.txt","w") as f2:
    for line in f1:
        if line.strip():
            f2.write(line)
