def grocery_store(**prdocuts):
    sorted_list = sorted(prdocuts.items(), key= lambda x: (-x[1], -len(x[0]), x[0]))
    list_of_sorted_products = []

    for product_name, qty in sorted_list:
        list_of_sorted_products.append(product_name)
        list_of_sorted_products += str(qty)

    return  "\n".join([str(x) for x in list_of_sorted_products])

print(grocery_store(
bread=5,
pasta=12,
eggs=12,
))