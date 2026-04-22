with open("log.txt", "r") as f:
    for line in f:
        if "ERROR" in line:
            print(line.strip())
