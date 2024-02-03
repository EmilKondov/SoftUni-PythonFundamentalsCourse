def accommodate_new_pets(hotel_capacity, max_weight, *args):
    pets = {}
    result = []

    for pet_type, weigh in args:
        if hotel_capacity <= 0:
            result.append(f"You did not manage to accommodate all pets!")
            break
        if weigh > max_weight:
            continue
        if pet_type not in pets:
            pets[pet_type] = []
        pets[pet_type].append(weigh)
        hotel_capacity -= 1
    else:
        result.append(f"All pets are accommodated! Available capacity: {hotel_capacity}.")

    result.append("Accommodated pets:")
    [result.append(f'{pet_type}: {len(weigh)}') for pet_type, weigh in sorted(pets.items())]
    return '\n'.join(result)

#1
print(accommodate_new_pets(
    10,
    15.0,
    ("cat", 5.8),
    ("dog", 10.0),
))
#
#
# #2
# print(accommodate_new_pets(
#     10,
#     10.0,
#     ("cat", 5.8),
#     ("dog", 10.5),
#     ("parrot", 0.8),
#     ("cat", 3.1),
# ))
#
#
# #3
# print(accommodate_new_pets(
#     2,
#     15.0,
#     ("dog", 10.0),
#     ("cat", 5.8),
#     ("cat", 2.7),
# ))



# if hotel_capacity != 0:
#     if weight <= max_weight:
#         if breed not in pets:
#             pets[breed] = []
#         pets[breed].append(weight)
#     else:
#         continue