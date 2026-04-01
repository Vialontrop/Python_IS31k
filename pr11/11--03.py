class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee(Person):
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = position


e = Employee("Alice", 30, "Teacher")
print(e.name, e.age, e.position)
