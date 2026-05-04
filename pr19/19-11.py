# Практическая работа 19 – Задача 11
# CPU-bound: тяжёлая математика в нескольких процессах

import multiprocessing
import time

def heavy_math(n):
    """Вычисляет сумму квадратов до n."""
    result = sum(i * i for i in range(n))
    print(f"[PID {multiprocessing.current_process().pid}] sum_sq({n}) = {result}")
    return result

if __name__ == "__main__":
    tasks = [5_000_000, 7_000_000, 6_000_000, 4_000_000]

    start = time.time()
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(heavy_math, tasks)
    elapsed = time.time() - start

    print(f"\nРезультаты: {results}")
    print(f"Время выполнения: {elapsed:.2f} сек")
