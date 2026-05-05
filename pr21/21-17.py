# Практическая работа 21 – Задача 17
# Timer со слотами и вычислением разницы времени

from datetime import datetime

class Timer:
    __slots__ = ('start', 'end')

    def __init__(self):
        self.start = None
        self.end   = None

    def begin(self):
        self.start = datetime.now()
        print(f"Старт: {self.start.strftime('%H:%M:%S.%f')}")

    def stop(self):
        if self.start is None:
            raise RuntimeError("Таймер не был запущен")
        self.end = datetime.now()
        print(f"Стоп:  {self.end.strftime('%H:%M:%S.%f')}")

    def elapsed(self):
        if self.start is None or self.end is None:
            raise RuntimeError("Таймер не завершён")
        delta = self.end - self.start
        return delta.total_seconds()


import time

t = Timer()
t.begin()
time.sleep(0.5)
t.stop()
print(f"Прошло: {t.elapsed():.3f} сек")
