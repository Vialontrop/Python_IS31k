from datetime import datetime

deadline = datetime(2026, 5, 1)
now = datetime.now()

if now > deadline:
    print("Просрочено")
else:
    print("Еще есть время")
