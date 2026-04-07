def calculator(a, b, op):
    try:
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return a / b
        else:
            return "Unknown operation"
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError:
        return "Type error"


print(calculator(5, 3, "+"))
print(calculator(5, 0, "/"))
print(calculator(5, 3, "^"))
print(calculator(5, "a", "+"))
