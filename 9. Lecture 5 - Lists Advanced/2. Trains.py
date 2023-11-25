number_of_wagons = int(input())
list_wagon = [0] * number_of_wagons

while True:
    command = input().split()
    if command[0] == 'End':
        print(list_wagon)
        break
    elif command[0] == 'add':
        number_of_people = int(command[1])
        list_wagon[-1] +=number_of_people
    elif command[0] == 'insert':
        index = int(command[1])
        number_of_people = int(command[2])
        list_wagon[index] += number_of_people
    elif command[0] == 'leave':
        index = int(command[1])
        number_of_people = int(command[2])
        list_wagon[index] -= number_of_people

