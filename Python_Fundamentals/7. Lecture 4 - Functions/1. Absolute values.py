    #1
# sequence_of_numbers = list(map(float, input().split()))
#
# list_of_abs_values = []
#
# for i in sequence_of_numbers:
#     list_of_abs_values.append(abs(i))
#
# print(list_of_abs_values)


    #2 Or
# numbers = input().split()
#
# list_of_absolute_values = []
#
# for i in numbers:
#     list_of_absolute_values.append(abs(float(i)))
#
# print(list_of_absolute_values)

    #3 OR by using a comprehension
absolute_values = print([abs(float(x)) for x in input().split()])