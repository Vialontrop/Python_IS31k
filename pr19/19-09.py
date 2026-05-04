# Практическая работа 19 – Задача 9
# Multiprocessing: 2 процесса считают сумму чисел от 1 до 100 000

import multiprocessing

def calc_sum(start, end, result_dict, key):
    total = sum(range(start, end + 1))
    result_dict[key] = total
    print(f"[Процесс-{key}] сумма [{start}..{end}] = {total}")

if __name__ == "__main__":
    manager = multiprocessing.Manager()
    results = manager.dict()

    p1 = multiprocessing.Process(target=calc_sum, args=(1, 100_000, results, 1))
    p2 = multiprocessing.Process(target=calc_sum, args=(1, 100_000, results, 2))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(f"Процесс 1: {results[1]}")
    print(f"Процесс 2: {results[2]}")
