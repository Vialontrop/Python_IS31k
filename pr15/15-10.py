with open("input.txt", "r") as f:
    lines = set(f.readlines())

with open("unique.txt", "w") as f:
    f.writelines(lines)
