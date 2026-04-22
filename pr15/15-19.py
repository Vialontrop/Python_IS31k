from datetime import datetime

message = "Test message"

with open("log.txt", "a") as f:
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    f.write(f"[{time}] {message}\n")
