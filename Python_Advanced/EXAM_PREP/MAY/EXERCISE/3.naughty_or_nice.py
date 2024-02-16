from collections import deque


def naughty_or_nice_list(data_list, *args, **kwargs):
    santa_list  = deque(data_list)
    commands = args
    keywords = kwargs

    nice = []
    naughty = []
    not_found = []

    command_dict = {}
    for pair in commands:
        key, value = pair.split("-")
        command_dict[key] = value
        

    for key in command_dict.keys():
        if santa_list.count(key) == 1:
            nice.append(santa_list[key].pop(value))
        elif str(key) in commands[1]:
            naughty.append(value)
        else:
            not_found.append(value)

       

# OUTPUT
    result = ''
    if nice:
        result += f"Nice: {', '.join(nice)}\n"
    if naughty:
        result += f"Naughty: {','.join(naughty)}\n"
    if not_found:
        result += f"Not found: {', '.join(not_found)}\n"

    # return result

    

print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))


# print(naughty_or_nice_list(
#  [
#  (7, "Peter"),
#  (1, "Lilly"),
#  (2, "Peter"),
#  (12, "Peter"),
#  (3, "Simon"),
#  ],
#  "3-Nice",
#  "5-Naughty",
#  "2-Nice",
#  "1-Nice",
#  ))
#
#
# print(naughty_or_nice_list(
#  [
#  (6, "John"),
#  (4, "Karen"),
#  (2, "Tim"),
#  (1, "Merry"),
#  (6, "Frank"),
#  ],
#  "6-Nice",
#  "5-Naughty",
#  "4-Nice",
#  "3-Naughty",
#  "2-Nice",
#  "1-Naughty",
#  Frank="Nice",
#  Merry="Nice",
#  John="Naughty",
# ))
#