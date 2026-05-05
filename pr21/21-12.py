# Практическая работа 21 – Задача 12
# User со слотами и методом изменения пароля

class User:
    __slots__ = ('login', 'password')

    def __init__(self, login, password):
        self.login    = login
        self.password = password

    def change_password(self, old_password, new_password):
        if old_password != self.password:
            raise ValueError("Неверный текущий пароль")
        if len(new_password) < 6:
            raise ValueError("Новый пароль слишком короткий (минимум 6 символов)")
        self.password = new_password
        print(f"[{self.login}] пароль успешно изменён")


u = User("alice", "secret")
u.change_password("secret", "newpass123")

try:
    u.change_password("wrongpass", "anotherpass")
except ValueError as e:
    print(e)

try:
    u.change_password("newpass123", "abc")
except ValueError as e:
    print(e)
