from datetime import datetime, timedelta

start = datetime(2024, 1, 1)
end = datetime(2024, 1, 10)

count = 0
current = start

while current <= end:
    if current.weekday() < 5:
        count += 1
    current += timedelta(days=1)

print(count)
