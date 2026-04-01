def logger(func):
    def wrapper():
        print(f"Calling {func.__name__}")
        func()
    return wrapper


def say_hello():
    print("Hello!")


say_hello = logger(say_hello)
say_hello()
