# Практическая работа 19 – Задача 12
# I/O-bound: потоковая загрузка файлов (имитация через sleep)

import threading
import time

def download_file(filename, delay):
    print(f"[Загрузка] Начало: {filename}")
    time.sleep(delay)   # имитация сетевой задержки
    print(f"[Загрузка] Готово: {filename} (заняло {delay} сек)")

files = [
    ("report.pdf", 2),
    ("image.png",  1),
    ("data.csv",   3),
    ("video.mp4",  4),
]

start = time.time()

threads = [threading.Thread(target=download_file, args=(f, d)) for f, d in files]
for t in threads: t.start()
for t in threads: t.join()

print(f"\nВсе файлы загружены за {time.time() - start:.1f} сек")
print(f"(последовательно заняло бы {sum(d for _, d in files)} сек)")
