def squares(n):
    i = 1
    end = n
    while i <= end:
        yield (i**2)
        i += 1



print(list(squares(5)))