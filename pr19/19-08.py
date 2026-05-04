# Практическая работа 19 – Задача 8
# Worker threads: пул потоков обрабатывает задачи из очереди

import threading
import queue
import time

NUM_WORKERS = 3
task_queue = queue.Queue()

def worker(worker_id):
    while True:
        task = task_queue.get()
        if task is None:
            print(f"[Worker-{worker_id}] завершает работу.")
            task_queue.task_done()
            break
        print(f"[Worker-{worker_id}] выполняет задачу #{task}")
        time.sleep(0.5)
        task_queue.task_done()

# Запускаем пул
workers = []
for i in range(NUM_WORKERS):
    t = threading.Thread(target=worker, args=(i + 1,))
    t.start()
    workers.append(t)

# Добавляем задачи
for task_id in range(1, 10):
    task_queue.put(task_id)

# Сигнал завершения для каждого воркера
for _ in range(NUM_WORKERS):
    task_queue.put(None)

task_queue.join()
for t in workers:
    t.join()

print("Все задачи выполнены.")
