# Практическая работа 19 – Задача 20
# Мини-система обработки задач: async workers + очередь + статус

import asyncio
import random
import time

NUM_WORKERS = 3
NUM_TASKS   = 10

async def worker(worker_id: int, queue: asyncio.Queue):
    while True:
        task_id = await queue.get()
        if task_id is None:
            print(f"  [Worker-{worker_id}] завершает работу.")
            queue.task_done()
            break

        delay = random.uniform(0.5, 2.0)
        print(f"  [Worker-{worker_id}] ▶ начало задачи #{task_id:02d} (ждать {delay:.1f}с)")
        await asyncio.sleep(delay)
        print(f"  [Worker-{worker_id}] ✓ задача #{task_id:02d} выполнена")
        queue.task_done()

async def main():
    queue = asyncio.Queue()

    # Заполняем очередь задачами
    for task_id in range(1, NUM_TASKS + 1):
        await queue.put(task_id)

    # Сигналы остановки для каждого воркера
    for _ in range(NUM_WORKERS):
        await queue.put(None)

    start = time.time()
    print(f"Запуск {NUM_WORKERS} воркеров для {NUM_TASKS} задач...\n")

    workers = [
        asyncio.create_task(worker(i + 1, queue))
        for i in range(NUM_WORKERS)
    ]

    await queue.join()
    await asyncio.gather(*workers)

    elapsed = time.time() - start
    print(f"\nВсе задачи выполнены за {elapsed:.1f} сек.")

asyncio.run(main())
