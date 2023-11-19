string_for_money = input().split(", ")
number_of_beggars = int(input())
integer_for_money = []
for element in string_for_money:
    integer_for_money.append(int(element))
final_sums = []
start_index = 0
while start_index < number_of_beggars:
    sum_for_current_beggar = 0
    for current_index in range(start_index, len(integer_for_money), number_of_beggars):
        sum_for_current_beggar += integer_for_money[current_index]
    final_sums.append(sum_for_current_beggar)
    start_index += 1
print(final_sums)
