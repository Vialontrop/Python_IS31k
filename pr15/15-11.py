from datetime import datetime

date = datetime.strptime("2024-12-31", "%Y-%m-%d")

print(date.day)
print(date.month)
print(date.year)
