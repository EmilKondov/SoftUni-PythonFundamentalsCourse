n = int(input())

def print_row(size, row):
    print(" " * (size - row), " *" * row)

def upper_part(size):
    for row in range(1, size + 1):
        print_row(size, row)

def down_part(size):
    for row in range(size - 1, 0, -1):
        print_row(size, row)


def print_rhombus(size):
    upper_part(size)
    down_part(size)

print_rhombus(n)
