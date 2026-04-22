from datetime import datetime, timedelta

date = datetime(2024, 4, 10)

while date.weekday() != 0:
    date += timedelta(days=1)

print(date)
