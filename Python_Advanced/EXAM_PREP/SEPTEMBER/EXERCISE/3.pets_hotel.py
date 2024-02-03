def accommodate_new_pets(hotel_capacity, max_weight, *args):
    pets = {}
    result = []

    for breed, weight in args:
        if hotel_capacity <= 0:
            result.append("You did not manage to accommodate all pets!")
            break
        if weight > max_weight:
            continue
        if breed not in pets:
            pets[breed] = []
        pets[breed].append(weight)
        hotel_capacity -= 1
    else:
        result.append(f"All pets are accommodated! Available capacity: {hotel_capacity}.")

    result.append(f"Accommodated pets:")
    [result.append(f"{breed}: {len(weight)}") for breed, weight in sorted(pets.items())]
    return "\n".join(result)

print(accommodate_new_pets(
    10,
    15.0,
    ("cat", 5.8),
    ("dog", 10.0),
))