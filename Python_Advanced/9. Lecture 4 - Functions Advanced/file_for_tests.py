# def names(**kwargs):
#     for key, value in kwargs.items():
#         print(f"My first name is {key} and my second name is {value}")
#
# names(Emil="Kondov", Margarit="Markov", Zhenya="Kondova")


# 1.Multiplication function:
#
# def multiply(*args):
#     sum = 1
#     for num in args:
#         sum *= num
#     return sum
#
# print(multiply(1, 4, 5))

#2. Person Info

# def get_info(name, age, town):
#     return f"This is {name} from {town} and he is {age} years old"
#
#
# print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))

#3.Cheese Showcase:

def sorting_cheeses(**kwargs):
    sorted_cheese = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))   # в аргумента на функцията (-len(x[1]), x[0]) е оградено с (), защото
                                                                               # по този начин казваме сортирай първо по критерии ..., и после по. Тоест соритрай по брой на елементи, но
                                                                               # ако броя на елементите е равен то тогава сортирай тези елементи по азбучен ред на тяхните ключове.
    """                                                                        
    С **kwargs получваме речник от данните, които сме получили, но в sorted(),
     когато използваме .items() речникът се превръща във tuple от key-value pairs <=> kvp! 
    """
    result = []

    for (key, value) in sorted_cheese:
        result.append(key)
        value_list = sorted(value, reverse=True)
        result += value_list
    return "\n".join([str(x) for x in result])
print(sorting_cheeses(Parmesan=[102, 120, 135],Camembert=[100, 100, 105, 500, 430],Mozzarella=[50, 125],))
print(sorting_cheeses(Parmigiano=[165, 215],Feta=[150, 515],Brie=[150, 125]))