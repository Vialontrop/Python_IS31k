# Практическая работа 19 – Задача 13
# Daemon threads: фоновый поток, работающий пока живёт основная программа

import threading
import time

def background_monitor():
    count = 0
    while True:
        count += 1
        print(f"[Демон] тик #{count}")
        time.sleep(1)

# daemon=True — поток завершится автоматически вместе с основным
daemon_thread = threading.Thread(target=background_monitor, daemon=True)
daemon_thread.start()

print("Основная программа работает 4 секунды...")
time.sleep(4)
print("Основная программа завершена. Демон будет остановлен автоматически.")
