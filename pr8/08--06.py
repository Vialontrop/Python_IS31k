class Employee:
    def salary(self):
        return 0


class FullTimeEmployee(Employee):
    def salary(self):
        return 5000


class PartTimeEmployee(Employee):
    def salary(self):
        return 2000


employees = [FullTimeEmployee(), PartTimeEmployee(), Employee()]
for e in employees:
    print(e.salary())
