# 18--13.py
with open("input.txt") as f1, open("numbered.txt","w") as f2:
    for i,line in enumerate(f1,1):
        f2.write(f"{i}: {line}")
