def integer_func(given_int):
    return int(given_int) * 2

def real_func(given_real):
    return float(given_real) * 1.5


def string_func(given_string):
    return f"${given_string}$"


first_line = input()
data = input()

if first_line == "int":
    result = integer_func(data)

elif first_line == "real":
    result = (f"{real_func(data):.2f}")

elif first_line == "string":
    result = string_func(data)

print(result)
