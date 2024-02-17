from collections import deque

amount_of_money = [int(x) for x in input().split()]  # stack
food_prices = deque([int(y) for y in input().split()])

total_food = len(food_prices)
food_counter = 0

while amount_of_money and food_prices:

    current_money = amount_of_money.pop()
    current_price = food_prices.popleft()

    if current_money == current_price:
        food_counter += 1

    elif current_money > current_price:
        food_counter += 1
        change = current_money - current_price
        if amount_of_money:
            amount_of_money[-1] += change
        else:
            amount_of_money.append(change)


if food_counter >= 4:
    print(f"Gluttony of the day! Henry ate {food_counter} foods.")
if food_counter < total_food and food_counter != 0:
    if food_counter == 1:
        print(f"Henry ate: {food_counter} food.")
    else:
        print(f"Henry ate: {food_counter} foods.")
if food_counter == 0:
    print(f"Henry remained hungry. He will try next weekend again.")
