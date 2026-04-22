from datetime import datetime

birth = input("Введите дату рождения (YYYY-MM-DD): ")

birth_date = datetime.strptime(birth, "%Y-%m-%d")
today = datetime.now()

days = (today - birth_date).days

print(days)
