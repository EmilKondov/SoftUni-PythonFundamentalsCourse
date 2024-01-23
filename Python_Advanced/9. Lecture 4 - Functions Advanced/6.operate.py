from functools import reduce
def operate(command, *args):
    return reduce(lambda x, y: eval(f"{x}{command}{y}"), args) ### втори вариан използвайки eval()
    # if command == "+":                                       # той интерпетира реалното действие но застрашава сигфурността.
    #     return reduce(lambda x, y: x + y, args)
    # elif command == "-":
    #     return reduce(lambda x, y: x - y, args)
    # elif command == "*":
    #     return reduce(lambda x, y: x * y, args)
    # elif command == "/":
    #     return reduce(lambda x, y: x / y, args)

print(operate("+", 1, 2, 3))
print(operate("/", 1, 2, 3,))
print(operate("*", 3, 4))
print(operate("/", 12, 4))



