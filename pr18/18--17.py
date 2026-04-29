# 18--17.py
with open("log.txt") as f:
    for line in f:
        if "ERROR" in line:
            print(line)
