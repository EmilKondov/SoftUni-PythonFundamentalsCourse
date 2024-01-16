count_of_sequences = 2
sequences = {}
for index in range(count_of_sequences):
    current_set = {int(x) for x in input().split()}
    sequences[index + 1] = current_set

number_of_command_lines = int(input())

for _ in range(number_of_command_lines):
    line_input = input().split()
    action = line_input[0]
    order = line_input[1]
    numbers = line_input[2:]
    if action == "Add":
        if order == "First":
            for number in numbers:
                sequences[1].add(int(number))
        elif order == "Second":
            for number in numbers:
                sequences[2].add(int(number))
    elif action == "Remove":
        if order == "First":
            for number in numbers:
                if int(number) in sequences[1]:
                    sequences[1].remove(int(number))
        elif order == "Second":
            for number in numbers:
                if int(number) in sequences[2]:
                    sequences[2].remove(int(number))
    elif action == "Check":
        if sequences[1].issubset(sequences[2]) or sequences[2].issubset(sequences[1]) :
            print(True)
        else:
            print(False)

print(*sorted(int(x) for x in sequences[1]), sep=", ")
print(*sorted(int(x) for x in sequences[2]), sep=", ")
