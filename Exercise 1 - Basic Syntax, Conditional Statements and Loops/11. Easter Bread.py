budget = float(input())
price_for_1kg_flour = float(input())

price_for_1_pack_of_eggs = 0.75 * price_for_1kg_flour
price_for_250ml_of_milk = (price_for_1kg_flour * 1.25) / 4

price_for_1_loave = price_for_1kg_flour + price_for_1_pack_of_eggs + price_for_250ml_of_milk

number_of_loaves_made = 0
collored_eggs_gathered = 0


while budget >= price_for_1_loave:
    budget -= price_for_1_loave
    number_of_loaves_made += 1
    collored_eggs_gathered += 3

    if number_of_loaves_made % 3 == 0:
        eggs_lost = number_of_loaves_made - 2
        collored_eggs_gathered -= eggs_lost

money_left = budget
print(f"You made {number_of_loaves_made} loaves of Easter bread! Now you have {collored_eggs_gathered} eggs and {money_left:.2f}BGN left.")
