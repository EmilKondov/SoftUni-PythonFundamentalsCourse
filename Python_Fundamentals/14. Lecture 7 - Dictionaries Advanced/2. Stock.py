data = input().split()

stock = {}

for i in range(0, len(data), 2):
    key = data[i]
    value = data[i + 1]
    stock[key] = int(value)

products_to_check = input().split()
# Here we check for each product
for product in products_to_check:
    if product in stock:
        print(f"We have {stock[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
