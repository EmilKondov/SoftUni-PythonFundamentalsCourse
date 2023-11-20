list_of_items = input().split("|")
budget = float(input())

price_is_valid = False
train_ticket = 150
clothes_max_price= 50.00
shoes_max_price = 35.00
accessories_max_price = 20.50
profit = 0
bought_items = []
bought_items_new_prices = []

for item in list_of_items:
    item = item.split("->")
    type_of_item = str.lower(item[0])
    price_of_item = float(item[1])

    if type_of_item == "clothes":
        if price_of_item <= clothes_max_price:
            price_is_valid = True
    elif type_of_item == "shoes":
        if price_of_item <= shoes_max_price:
            price_is_valid = True
    elif type_of_item == "accessories":
        if price_of_item <= accessories_max_price:
            price_is_valid = True
    if price_is_valid:
        if budget >= price_of_item:
           budget -= price_of_item
           new_price_of_item = price_of_item * 1.40
           profit += new_price_of_item - price_of_item
           bought_items.append(type_of_item)
           bought_items_new_prices.append(new_price_of_item)

print(" ".join([f"{new_price_of_item:.2f}" for new_price_of_item in bought_items_new_prices]))
print(f"Profit: {profit:.2f}")
total_income = budget + sum(bought_items_new_prices)

if total_income >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
    