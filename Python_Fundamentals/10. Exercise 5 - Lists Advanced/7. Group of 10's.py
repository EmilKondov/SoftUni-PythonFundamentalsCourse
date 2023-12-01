sequence_of_numbers = [int(x) for x in input().split(", ")]
current_group_of_numbers = 10
while sequence_of_numbers: # while len(sequence_of_numbers) >0
    filtered_list_for_current_group = []
    for number in sequence_of_numbers:
        if number <= 10:
            filtered_list_for_current_group.append(number)
            