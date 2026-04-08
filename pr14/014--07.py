def print_info(**kwargs: str) -> None:
    for k, v in kwargs.items():
        print(f"{k}: {v}")

data = {'name': 'Bob', 'age': '25'}
print_info(**data)