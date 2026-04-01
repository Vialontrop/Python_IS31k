def repeat(n):
    def decorator(func):
        def wrapper():
            for _ in range(n):
                func()
        return wrapper
    return decorator


@repeat(3)
def greet():
    print("Hi!")


greet()
