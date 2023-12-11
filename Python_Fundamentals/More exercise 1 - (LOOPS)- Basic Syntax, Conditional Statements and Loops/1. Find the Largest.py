given_number = input()
sorted_num = sorted(given_number, reverse = True)
find_str = ""

for i in range(len(given_number)):
    find_str += sorted_num[i]

print(int(find_str))

