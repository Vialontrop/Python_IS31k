# Практическая работа 19 – Задача 5
# Демонстрация гонки потоков: общий счётчик без блокировок

import threading

counter = 0

def increment():
    global counter
    for _ in range(100_000):
        counter += 1   # не атомарная операция → гонка!

threads = [threading.Thread(target=increment) for _ in range(5)]

for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"Ожидалось: {5 * 100_000}")
print(f"Получено:  {counter}")
print("Разница из-за гонки потоков!" if counter != 500_000 else "Повезло — нет потерь (редко).")
