from datetime import datetime

now = datetime.now()

timestamp = now.timestamp()
print(timestamp)

converted = datetime.fromtimestamp(timestamp)
print(converted)
