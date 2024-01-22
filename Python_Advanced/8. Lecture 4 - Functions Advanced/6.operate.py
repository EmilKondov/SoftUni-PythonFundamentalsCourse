def operate(*args):
    command, *values = args
    if command == "+":
        sum = 0
        for num in values:
            sum += num

    elif command == "-":
        sum = 0
        for num in values:
            sum -= num

    elif command == "*":
        sum = 1
        for num in values:
            sum *= num

    elif command == "/":
        sum = 0
        for num in values:
            if num == 0:
                # sum = 0
                continue
            if sum == 0:
                sum = num
            else:
                sum /= num
    return  sum


#print(operate("+", 1, 2, 3))
#print(operate("/", 1, 0, 2, 3, 0))
#print(operate("*", 3, 4))
#print(operate("/", 12, 4))