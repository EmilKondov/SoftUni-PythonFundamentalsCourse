entry_data = int(input())

left_sum = 0
right_sum = 0

for i in range(1, entry_data + 1):
    left_sum += int(input())
for j in range(1, entry_data +1):
    right_sum += int(input())

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {abs(left_sum - right_sum)}")