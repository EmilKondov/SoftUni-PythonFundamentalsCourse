def odd_and_even_sum(some_number):
    sum_of_odd_digits = 0
    sum_of_even_digits = 0
    for current_digit in some_number:
        if int(current_digit) % 2 == 0:
            sum_of_even_digits += int(current_digit)
        elif int(current_digit) % 2 !=0:
            sum_of_odd_digits += int(current_digit)
    return f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"

single_number = input()
result = odd_and_even_sum(single_number)
print(result)
