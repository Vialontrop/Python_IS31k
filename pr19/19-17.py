# Практическая работа 19 – Задача 17
# Асинхронные задержки: 5 задач с разными задержками, порядок завершения

import asyncio
import time

async def delayed_task(name, delay):
    await asyncio.sleep(delay)
    print(f"{name} завершён через {delay}с  (время: {time.strftime('%H:%M:%S')})")

async def main():
    tasks = [
        delayed_task("Задача-A", 3),
        delayed_task("Задача-B", 1),
        delayed_task("Задача-C", 4),
        delayed_task("Задача-D", 0.5),
        delayed_task("Задача-E", 2),
    ]
    print("Запуск задач...\n")
    await asyncio.gather(*tasks)
    print("\nВсе задачи выполнены.")

asyncio.run(main())
