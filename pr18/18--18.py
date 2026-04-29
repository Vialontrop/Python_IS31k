# 18--18.py
with open("log.txt") as f:
    print(sum(1 for line in f if "ERROR" in line))
