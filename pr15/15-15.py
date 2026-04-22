from datetime import datetime

dates = ["2024-01-05", "2023-12-31", "2024-02-10"]

dates.sort(key=lambda x: datetime.strptime(x, "%Y-%m-%d"))

print(dates)
