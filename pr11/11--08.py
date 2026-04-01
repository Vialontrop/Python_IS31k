def check_positive(func):
    def wrapper(*args):
        for value in args:
            if value < 0:
                print("Error")
                return
        func(*args)
    return wrapper


@check_positive
def multiply(a, b):
    print(a * b)


multiply(3, 4)
multiply(3, -1)
