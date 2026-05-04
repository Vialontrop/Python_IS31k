# Практическая работа 19 – Задача 16
# asyncio.gather: выполнение нескольких задач одновременно

import asyncio

async def fetch_data(source, delay):
    print(f"[{source}] начало запроса...")
    await asyncio.sleep(delay)
    result = f"данные из {source}"
    print(f"[{source}] получено!")
    return result

async def main():
    results = await asyncio.gather(
        fetch_data("API-1", 1),
        fetch_data("API-2", 2),
        fetch_data("API-3", 0.5),
    )
    print("\nВсе результаты:")
    for r in results:
        print(f"  → {r}")

asyncio.run(main())
