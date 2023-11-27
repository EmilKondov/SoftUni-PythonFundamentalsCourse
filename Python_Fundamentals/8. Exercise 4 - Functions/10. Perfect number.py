def is_perfect(given_number: int):
    divisor_sum = 0
    for divisor in range(1, given_number):
        if given_number % divisor == 0:
            divisor_sum += divisor
            if divisor_sum == given_number:
                return 'We have a perfect number!'
    return "It's not so perfect."


number = int(input())
print(is_perfect(number))
