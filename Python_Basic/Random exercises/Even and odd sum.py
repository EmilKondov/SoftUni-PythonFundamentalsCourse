number = int(input())

sum_of_even = 0
sum_of_odd = 0

for i in range(1, number + 1):
    current_number = int(input())
    if i % 2 == 0:
        sum_of_even += current_number
    elif i % 2 != 0:
        sum_of_odd += current_number

if sum_of_even == sum_of_odd:
    print("Yes")
else:
    print(f"No \nDiff = {abs(sum_of_even - sum_of_odd)}")
