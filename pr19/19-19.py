# Практическая работа 19 – Задача 19
# Producer / Consumer (async) через asyncio.Queue

import asyncio
import random

async def producer(queue: asyncio.Queue, count: int):
    for i in range(1, count + 1):
        item = f"данные-{i}"
        await queue.put(item)
        print(f"[Producer] поместил: {item}")
        await asyncio.sleep(random.uniform(0.2, 0.6))
    await queue.put(None)   # сигнал завершения

async def consumer(queue: asyncio.Queue):
    while True:
        item = await queue.get()
        if item is None:
            print("[Consumer] получен сигнал завершения.")
            queue.task_done()
            break
        print(f"[Consumer] обрабатывает: {item}")
        await asyncio.sleep(0.8)   # имитация обработки
        queue.task_done()

async def main():
    q = asyncio.Queue(maxsize=3)
    await asyncio.gather(
        producer(q, count=7),
        consumer(q),
    )
    print("Готово.")

asyncio.run(main())
