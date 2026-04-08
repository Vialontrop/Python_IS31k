def multiply_all(*args: int) -> int:
    result = 1
    for n in args:
        result *= n
    return result

print(multiply_all(2, 3, 4))