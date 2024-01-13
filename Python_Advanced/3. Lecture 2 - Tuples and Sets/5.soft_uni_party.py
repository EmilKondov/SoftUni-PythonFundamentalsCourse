count_of_guests = int(input())

list_of_guests = set()

for guest in range(count_of_guests):
    list_of_guests.add(input())

command = input()
while command != "END":
    if command in list_of_guests:
        list_of_guests.remove(command)
    command = input()

print(len(list_of_guests))
for guest in sorted(list_of_guests):   # тук не сортираме сета, а взимаме сета и неговите елементи, сортираме елементите му и ги слагаме в лист. Сета сам по себе си не може да се сортира, тъй като не е подредена колекция.
    print(guest)
