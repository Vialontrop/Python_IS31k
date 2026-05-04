# Практическая работа 19 – Задача 6
# Lock (блокировка): исправляем гонку потоков

import threading

counter = 0
lock = threading.Lock()

def safe_increment():
    global counter
    for _ in range(100_000):
        with lock:          # только один поток в критической секции
            counter += 1

threads = [threading.Thread(target=safe_increment) for _ in range(5)]

for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"Ожидалось: {5 * 100_000}")
print(f"Получено:  {counter}")
print("Результат корректен!" if counter == 500_000 else "Что-то пошло не так.")
