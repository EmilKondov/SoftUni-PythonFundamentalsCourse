number_of_names = int(input())

list_of_names = []

for name in range(number_of_names):
    list_of_names.append(input())

unique_names = set(list_of_names)

for name in unique_names:
    print(name)


#### CHeck second solution ####