def sorting_cheeses(**cheese):
    cheese = sorted(cheese.items(), key = lambda x: (-len(x[1]), x[0]))

    result = []

    for cheese_name, values in cheese:
        result.append(cheese_name)
        values_list = sorted(values, reverse=True)
        result += values_list

    return "\n".join([str(x) for x in result])


print(
sorting_cheeses(
Parmesan=[102, 120, 135],
Camembert=[100, 100, 105, 500, 430],
Mozzarella=[50, 125],
)
)