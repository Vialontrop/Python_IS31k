class EmailAccount:
    def __init__(self):
        self._email = ""

    def set_email(self, email):
        if "@" in email:
            self._email = email

    def get_email(self):
        return self._email

account = EmailAccount()
account.set_email("user@example.com")
print(account.get_email())
account.set_email("wrongemail.com")
print(account.get_email())
