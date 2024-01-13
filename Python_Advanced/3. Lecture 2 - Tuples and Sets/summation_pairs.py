# import time
# numbers = [int(x) for x in input().split()]
# target_number = int(input())
#
# start = time.time()
# for i in range(len(numbers)):
#     if numbers[i] == "":
#         continue
#     for j in range(i + 1, len(numbers)):
#         if numbers[j] == "":
#             continue
#         if numbers[i] + numbers[j] == target_number:
#             print(f"{numbers[i]} + {numbers[j]} = {target_number}")
#             numbers[i] = ""
#             numbers[j] = ""
#             break
# end = time.time()
# print(f"Time range: {end-start}")

### Faster soltuion ###
import time

numbers = list(map(int, input().split()))
target = int(input())

start = time.time()
targets = set()
value_map = {}

for value in numbers:
    if value in targets:
        targets.remove(value)
        pair = value_map[value]
        del value_map[value]
        print(f'{pair} + {value} = {target}')
    else:
        resulting_number = target - value
        targets.add(resulting_number)
        value_map[resulting_number] = value
end = time.time()
print(f"Time range: {end-start}")