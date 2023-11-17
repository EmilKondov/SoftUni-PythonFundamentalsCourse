number_of_snowballs = int(input())

max_snowball_weight = 0
max_time = 0
max_value = 0
max_quality = 0


for current_snowball in range(number_of_snowballs):
    weight_of_snowball = int(input())
    time_to_target = int(input())
    quality_of_snowball = int(input())
    value_for_current_snowball = (weight_of_snowball // time_to_target) ** quality_of_snowball
    if value_for_current_snowball > max_value:
        max_value = value_for_current_snowball
        max_time = time_to_target
        max_snowball_weight = weight_of_snowball
        max_quality = quality_of_snowball
    else:
        continue
print(f"{max_snowball_weight} : {max_time} = {max_value} ({max_quality})")
