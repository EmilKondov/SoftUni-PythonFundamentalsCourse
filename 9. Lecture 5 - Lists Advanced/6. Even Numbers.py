given_numbers = list(map(int, input().split(", ")))

even_numbers = map(lambda x: x if given_numbers[x] % 2 == 0 else 'no', range(len(given_numbers)))
even_indices = list(filter(lambda a: a != 'no', even_numbers))
print(even_indices)
 