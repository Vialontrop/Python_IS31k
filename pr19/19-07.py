# Практическая работа 19 – Задача 7
# Очередь задач: queue.Queue для передачи данных между потоками

import threading
import queue
import time

q = queue.Queue()

def producer():
    for i in range(1, 6):
        print(f"[Producer] отправляю: {i}")
        q.put(i)
        time.sleep(0.5)
    q.put(None)   # сигнал завершения

def consumer():
    while True:
        item = q.get()
        if item is None:
            print("[Consumer] получен сигнал завершения.")
            break
        print(f"[Consumer] обработал: {item}")
        q.task_done()

t_prod = threading.Thread(target=producer)
t_cons = threading.Thread(target=consumer)

t_prod.start()
t_cons.start()

t_prod.join()
t_cons.join()
print("Готово.")
