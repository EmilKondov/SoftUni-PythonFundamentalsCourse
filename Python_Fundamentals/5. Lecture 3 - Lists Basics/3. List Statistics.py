given_number_n = int(input())

positive_numbers_lst = []
negative_numbers_lst = []

for current_number in range(given_number_n):
    current_number = int(input())
    if current_number > 0:
        positive_numbers_lst.append(current_number)
    else:
        negative_numbers_lst.append(current_number)

print(positive_numbers_lst)
print(negative_numbers_lst)

print(f"Count of positives: {len(positive_numbers_lst)}")
print(f"Sum of negatives: {sum(negative_numbers_lst)}")
