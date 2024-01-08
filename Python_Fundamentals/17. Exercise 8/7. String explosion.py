initial_string = input()
new_string = ""
strenght = 0

for index in range(len(initial_string)):
    if strenght > 0 and initial_string[index] != ">":
        strenght -= 1
    elif initial_string[index] == ">":
        new_string += initial_string[index]
        strenght += int(initial_string[index + 1])
    else:
        new_string += initial_string[index]
print(new_string)