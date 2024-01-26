for i in range(5):
    given_number = int(input())

    if given_number < 0:
        ValueCannotBeNegative = ValueError("ValueCannotBeNegative")
        raise ValueCannotBeNegative
    else:
        continue
