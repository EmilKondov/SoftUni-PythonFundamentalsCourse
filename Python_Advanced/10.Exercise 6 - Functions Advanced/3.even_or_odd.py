def even_odd(*args):
    if command == "even":
        return [int(x) for x in kwargs if x % 2 ==0]
    elif command == "odd":
        return [int(x) for x in kwargs if x % 2 != 0]




print(even_odd(1, 2, 3, 4, 5, 6, "even"))
#print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))