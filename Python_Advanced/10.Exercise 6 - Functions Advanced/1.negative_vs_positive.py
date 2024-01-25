def positive(numbers):
    sum_positive = 0
    for number in numbers:
        if number > 0:
            sum_positive += number
    return sum_positive

def negative(numbers):
    sum_negative = 0
    for number in numbers:
        if number < 0:
            sum_negative += number
    return sum_negative

def negative_or_positive(numbers):
    if abs(positive(numbers)) > abs(negative(numbers)):
        return "The positives are stronger than the negatives"
    else:
        return "The negatives are stronger than the positives"



line_of_numbers = [int(x) for x in input().split()]
print(negative(line_of_numbers))
print(positive(line_of_numbers))
print(negative_or_positive(line_of_numbers))
