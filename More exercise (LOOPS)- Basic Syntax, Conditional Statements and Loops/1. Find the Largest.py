given_number = int(input())

given_number_str = str(given_number)
sorted_num = sorted(given_number_str, reverse = True)
fina_str = ""

for i in range(len(given_number_str)):
    fina_str += sorted_num[i]

print(int(fina_str))
