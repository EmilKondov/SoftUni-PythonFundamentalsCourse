def calculate_price(product, quantity):
    if product == 'coffee':
        return coffee_price * quantity
    elif product == 'coke':
        return  coke_price * quantity
    elif product == 'water':
        return  water_price * quantity
    elif product == 'snacks':
        return  snacks_price * quantity



coffee_price = 1.50
water_price = 1.00
coke_price = 1.40
snacks_price = 2.00

product = input()
quantity = int(input())
result = calculate_price(product, quantity)
print(f"{result:.2f}")
