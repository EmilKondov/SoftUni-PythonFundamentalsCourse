def min_and_max(some_numbers):
    return f'The minimum number is {min(some_numbers)} \nThe maximum number is {max(some_numbers)} \nThe sum number is: {sum(some_numbers)}'

sequence_of_numbers = list(map(int, input().split()))
print(min_and_max(sequence_of_numbers))
