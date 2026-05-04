# Практическая работа 19 – Задача 10
# Сравнение скорости: threading vs multiprocessing

import threading
import multiprocessing
import time

def cpu_task():
    return sum(i * i for i in range(1_000_000))

# --- Threading ---
start = time.time()
threads = [threading.Thread(target=cpu_task) for _ in range(4)]
for t in threads: t.start()
for t in threads: t.join()
thread_time = time.time() - start
print(f"Threading:      {thread_time:.3f} сек")

# --- Multiprocessing ---
if __name__ == "__main__":
    start = time.time()
    processes = [multiprocessing.Process(target=cpu_task) for _ in range(4)]
    for p in processes: p.start()
    for p in processes: p.join()
    mp_time = time.time() - start
    print(f"Multiprocessing:{mp_time:.3f} сек")

    print("\nВывод: для CPU-bound задач multiprocessing быстрее,")
    print("т.к. обходит GIL и использует несколько ядер.")
