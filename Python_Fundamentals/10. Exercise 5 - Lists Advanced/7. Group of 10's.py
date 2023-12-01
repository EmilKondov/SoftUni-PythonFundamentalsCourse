numbers = [int(x) for x in input().split(", ")]

current_group_of_numbers = 10

while numbers: # while len(numbers) > 0
    filtered_list_current_group = []
    for number in numbers:
        if number <= current_group_of_numbers:
            filtered_list_current_group.append(number)
    print(f"Group of {current_group_of_numbers}'s: {filtered_list_current_group}")
    current_group_of_numbers += 10
    numbers = [number for number in numbers if number not in filtered_list_current_group]
