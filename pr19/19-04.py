# Практическая работа 19 – Задача 4
# Задержка в потоках: time.sleep меняет порядок выполнения

import threading
import time

def fast_task():
    for i in range(1, 4):
        print(f"[Быстрый] шаг {i}")
        time.sleep(0.2)

def slow_task():
    for i in range(1, 4):
        print(f"[Медленный] шаг {i}")
        time.sleep(1)   # длинная задержка

t1 = threading.Thread(target=fast_task)
t2 = threading.Thread(target=slow_task)

print("Запуск потоков...")
t1.start()
t2.start()

t1.join()
t2.join()

print("Готово. Обратите внимание: быстрый поток обогнал медленный.")
