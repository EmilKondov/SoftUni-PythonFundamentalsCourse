def merge(text, first_index, endindex_or_partition):
    list_of_characters = []
    for element in text:
        index_of_element = text.index(element)
        if index_of_element in range(int(first_index), int(list_of_characters)):
            list_of_characters.append(element)
    "".join(list_of_characters)
    return list_of_characters


def divide(text, first_index, endindex_or_partition):
    pass






text = input().split()

command = input()

while command != "3:1":
    command = command.split()
    action, first_index, endindex_or_partition = command[0], command[1], command[2]
    if action == "merge":
        text = merge(text,first_index,endindex_or_partition)
    elif action == "divide":
        text = divide(text,first_index,endindex_or_partition)


    command = input()
