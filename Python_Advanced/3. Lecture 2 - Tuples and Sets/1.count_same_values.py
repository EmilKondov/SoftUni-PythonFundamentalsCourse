numbers = tuple([float(x) for x in input().split()])

same_numbers = {}

for number in numbers:
    if number not in same_numbers:
        same_numbers[number] = numbers.count(number)

for number, occurences  in same_numbers.items():
    print(f"{number} - {occurences} times")
