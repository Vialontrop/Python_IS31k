# Практическая работа 19 – Задача 15
# Несколько задач asyncio параллельно

import asyncio

async def task(name, delay):
    print(f"[{name}] старт")
    await asyncio.sleep(delay)
    print(f"[{name}] завершён (задержка {delay}с)")

async def main():
    t1 = asyncio.create_task(task("Задача-1", 1))
    t2 = asyncio.create_task(task("Задача-2", 2))
    t3 = asyncio.create_task(task("Задача-3", 0.5))

    await t1
    await t2
    await t3

asyncio.run(main())
