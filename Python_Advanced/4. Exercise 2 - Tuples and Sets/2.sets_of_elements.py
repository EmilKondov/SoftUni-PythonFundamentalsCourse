sets_lenght = [int(x) for x in input().split()]
first_set_lenght, second_set_lenght = sets_lenght
sets_items = []
for item in range(first_set_lenght + second_set_lenght):
    sets_items.append(int(input()))

first_set = set(sets_items[:first_set_lenght])
second_set = set(sets_items[first_set_lenght:])

# for element in first_set.intersection(second_set):
#     print(element)


### Or by using intersection operator & 

for element in first_set & second_set:
    print(element)