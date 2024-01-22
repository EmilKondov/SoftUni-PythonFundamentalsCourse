# given_list = input().split("|")
#
# sub_list = []
#
# for sub_string in given_list[::-1]:   # чрез слайсинг казвам да започне от последния елемент да върти цикъла в обратен ред.
#     sub_list.extend(sub_string.split())
#
# print(*sub_list)
#


### Solution 2

numbers = [string.split() for string in input().split("|")]

print(*[' '.join(sub_list) for sub_list in numbers[::-1] if sub_list])

