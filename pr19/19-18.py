# Практическая работа 19 – Задача 18
# Асинхронное чтение файлов (имитация с задержкой)

import asyncio

async def read_file(filename, delay):
    print(f"[Чтение] Открываю {filename}...")
    await asyncio.sleep(delay)   # имитация дискового I/O
    content = f"<содержимое {filename}>"
    print(f"[Чтение] {filename} прочитан ({delay}с): {content}")
    return content

async def main():
    files = [
        ("config.json", 0.5),
        ("data.csv",    1.5),
        ("log.txt",     1.0),
        ("report.pdf",  2.0),
    ]

    print("Начинаем асинхронное чтение файлов...\n")
    results = await asyncio.gather(*[read_file(f, d) for f, d in files])

    print("\nИтог — все файлы прочитаны:")
    for r in results:
        print(f"  {r}")

asyncio.run(main())
