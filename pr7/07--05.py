class BankAccount:
    def __init__(self):
        self._balance = 0

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount

    def get_balance(self):
        return self._balance

account = BankAccount()
account.deposit(100)
account.withdraw(30)
print(account.get_balance())
account.withdraw(100)
print(account.get_balance())
