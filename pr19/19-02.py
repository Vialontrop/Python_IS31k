# Практическая работа 19 – Задача 2
# Потоки (threading): две функции печатают числа от 1 до 5

import threading
import time

def print_numbers(name):
    for i in range(1, 6):
        print(f"[{name}] {i}")
        time.sleep(0.5)

t1 = threading.Thread(target=print_numbers, args=("Поток-1",))
t2 = threading.Thread(target=print_numbers, args=("Поток-2",))

t1.start()
t2.start()

t1.join()
t2.join()

print("Оба потока завершены.")
