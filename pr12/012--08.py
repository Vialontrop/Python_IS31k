def process_data(a, b):
    try:
        a = int(a)
        b = int(b)
        try:
            return a / b
        except ZeroDivisionError:
            return "Division by zero"
    except ValueError:
        return "Conversion error"


print(process_data("10", "2"))
print(process_data("10", "0"))
print(process_data("a", "2"))
