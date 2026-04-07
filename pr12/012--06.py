def safe_sum(lst):
    total = 0
    for item in lst:
        try:
            total += item
        except TypeError:
            pass
    return total


print(safe_sum([1, 2, "a", 3]))
