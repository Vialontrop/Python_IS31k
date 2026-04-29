# 18--16.py
from datetime import datetime
with open("log.txt","a") as f:
    f.write(f"{datetime.now()} - INFO\n")
