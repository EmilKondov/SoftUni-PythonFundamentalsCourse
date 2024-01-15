value = 0
current_sum = 0
set_of_even = set()
set_of_odd = set()


for row in range(1, int(input()) + 1):
    name = input()
    for ch in name:
        value += ord(ch)
    current_sum = value // row
    if current_sum % 2 == 0:
        set_of_even.add(current_sum)
    else:
        set_of_odd.add(current_sum)
    current_sum = 0
    value = 0

sum_of_even_set = sum(set_of_even)
sum_of_odd_set = sum(set_of_odd)

if sum_of_even_set == sum_of_odd_set:
    print(*set_of_even.union(set_of_odd), sep=", ")
elif sum_of_odd_set > sum_of_even_set:
    print(*set_of_odd.difference(set_of_even), sep=", ")
else:
    print(*set_of_odd.symmetric_difference(set_of_even), sep=", ")
