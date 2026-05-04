# Практическая работа 19 – Задача 3
# Проверка работы потоков: 3 потока печатают своё имя 5 раз

import threading
import time

def print_name(name):
    for _ in range(5):
        print(f"Меня зовут: {name}")
        time.sleep(0.3)

threads = []
names = ["Алиса", "Боб", "Карлос"]

for name in names:
    t = threading.Thread(target=print_name, args=(name,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Все потоки завершены.")
