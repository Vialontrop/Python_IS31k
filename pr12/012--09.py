def safe_print_number(s):
    try:
        number = int(s)
    except ValueError:
        print("Error")
    else:
        print(number)


safe_print_number("5")
safe_print_number("abc")
