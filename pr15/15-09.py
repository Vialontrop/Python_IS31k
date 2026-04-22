with open("result.txt", "w") as result:
    for filename in ["file1.txt", "file2.txt"]:
        with open(filename, "r") as f:
            result.write(f.read())
