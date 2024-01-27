def grocery_store(**prdocuts):
    sorted_list = sorted(prdocuts.items(), key= lambda x: (-x[1], -len(x[0]), x[0]))

    list_of_sorted_products = []

    for product_name, qty in sorted_list:                                       # чрез f стринг добавяме всеки два елемента от sorted_list като единичен стринг и получаваме лист от 3 отделни елемента- стрингове.
        list_of_sorted_products.append(f"{product_name}: {qty}")

    return "\n".join(list_of_sorted_products)                                   #принтираме всеки елемент от листа на нов ред

print(grocery_store(
bread=5,
pasta=12,
eggs=12,
))
