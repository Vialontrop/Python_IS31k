# Практическая работа 19 – Задача 1
# Псевдомногозадачность: последовательное vs параллельное выполнение

import time

def task1():
    print("task1: шаг 1")
    time.sleep(1)
    print("task1: шаг 2")
    time.sleep(1)
    print("task1: шаг 3")

def task2():
    print("task2: шаг 1")
    time.sleep(1)
    print("task2: шаг 2")
    time.sleep(1)
    print("task2: шаг 3")


print("=== Последовательное выполнение ===")
start = time.time()
task1()
task2()
print(f"Время: {time.time() - start:.2f} сек\n")

# При параллельном — функции чередуются (через потоки/asyncio)
# Пример «псевдопараллельного» через генераторы
def task1_gen():
    print("task1: шаг 1"); yield
    print("task1: шаг 2"); yield
    print("task1: шаг 3"); yield

def task2_gen():
    print("task2: шаг 1"); yield
    print("task2: шаг 2"); yield
    print("task2: шаг 3"); yield

print("=== Псевдопараллельное (кооперативное) выполнение ===")
t1 = task1_gen()
t2 = task2_gen()
tasks = [t1, t2]
while tasks:
    for t in tasks[:]:
        try:
            next(t)
        except StopIteration:
            tasks.remove(t)
