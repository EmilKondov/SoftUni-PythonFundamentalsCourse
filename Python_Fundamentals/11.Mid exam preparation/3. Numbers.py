numbers = [int(x) for x in input().split()]
average = sum(numbers) / len(numbers)
top_numbers = []

for number in numbers:
    if number > average:
        top_numbers.append(number)


if len(top_numbers) == 0:
    print('No')
else:
    result = (sorted(top_numbers, reverse=True))
    print(*result[0:5])
