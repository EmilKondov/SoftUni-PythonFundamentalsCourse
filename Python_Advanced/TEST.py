number_of_lines = int(input())

sets = {}
for given_range in range(number_of_lines):
    list_of_ranges = [[int(x) for x in x.split(',')] for x in input().split('-')]
    first_list_of_ranges = list_of_ranges[0]
    second_list_of_ranges = list_of_ranges[1]
    sets[given_range] = []
    for number in range(first_list_of_ranges[0], first_list_of_ranges[-1] + 1):
        sets[given_range].append(number)
    for number in range(second_list_of_ranges[0], second_list_of_ranges[-1] + 1):
        sets[given_range].append(number)


