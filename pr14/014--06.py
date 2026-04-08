def print_info(**kwargs: str) -> None:
    for k, v in kwargs.items():
        print(f"{k}: {v}")

print_info(name='Alice', city='Paris')