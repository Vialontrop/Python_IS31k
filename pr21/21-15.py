# Практическая работа 21 – Задача 15
# BankAccount со слотами: пополнение и снятие с проверкой баланса

class BankAccount:
    __slots__ = ('balance',)

    def __init__(self, initial_balance=0):
        if initial_balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным")
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")
        self.balance += amount
        print(f"Пополнение: +{amount}. Баланс: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if amount > self.balance:
            raise ValueError(f"Недостаточно средств: баланс {self.balance}, запрошено {amount}")
        self.balance -= amount
        print(f"Снятие: -{amount}. Баланс: {self.balance}")


acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(200)
print(f"Итоговый баланс: {acc.balance}")

try:
    acc.withdraw(5000)
except ValueError as e:
    print(e)
