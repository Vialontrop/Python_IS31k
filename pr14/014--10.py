def process(a: int, b: int, *args: int, **kwargs: int) -> int:
    total = a + b
    total += sum(args)
    total += sum(kwargs.values())
    return total

print(process(1, 2, 3, 4, x=5, y=6))