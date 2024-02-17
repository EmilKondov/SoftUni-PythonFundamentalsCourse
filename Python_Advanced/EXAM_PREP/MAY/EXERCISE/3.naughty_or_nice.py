def naughty_or_nice_list(santa_list, *args, **kwargs):
    nice = []
    naughty = []
    result = []

    def kids_sorting():
        if len(kids) == 1:
            nice.append(kids[0][1]) if type_of_kid == "Nice" else naughty.append(kids[0][1])
            santa_list.remove(kids[0])


    for info in args:
        number, type_of_kid = info.split("-")
        kids = [element for element in santa_list if element[0] == int(number)]
        kids_sorting()

    for name, type_of_kid in kwargs.items():
        kids = [element for element in santa_list if element[1] == name]
        kids_sorting()

# OUTPUT
    if nice:
        result.append(f"Nice: {', '.join(nice)}")
    if naughty:
        result.append(f"Naughty: {', '.join(naughty)}")
    if santa_list:
        result.append(f"Not found: {', '.join(k[1] for k in santa_list)}")

    return '\n'.join(result)
