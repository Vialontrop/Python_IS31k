# Практическая работа 19 – Задача 14
# Простая async функция с asyncio.sleep

import asyncio

async def greet(name):
    print(f"[{name}] Привет! Жду 1 секунду...")
    await asyncio.sleep(1)
    print(f"[{name}] Сообщение после ожидания!")

async def main():
    await greet("Алиса")

asyncio.run(main())
