numbers = [int(x) for x in input().split()]        #FIRST_COUNT = 5
average = sum(numbers) / len(numbers)              #
top_numbers = []                                   #
                                                   # Second option is to use only comprehension
for number in numbers:                             # top_numbers = sorted[x for x in numbers if x >avg_num]
    if number > average:                           #
        top_numbers.append(number)                 #  if not top_numbers:
                                                   #    print('No')
                                                   #  else:
if len(top_numbers) == 0:                          #    for i in range(FIRST_COUNT):
    print('No')                                    #        if top_numbers:
else:                                              #           print(top_numbers.pop(), end = " ")
    result = (sorted(top_numbers, reverse=True))   #
    print(*result[0:5])                            #  other option using long comprehension:  print(*[top_numbers.pop() for i in range(FIRST_COUNT) if top_numbers])





