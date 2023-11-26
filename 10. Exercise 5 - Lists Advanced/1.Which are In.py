#first_sequence = input().split(", ")
#second_sequence = input().split(", ")
#substrings = []
#for word in first_sequence:
#    for other_word in second_sequence:
#        if word in other_word:
#            substrings.append(word)
#            break
#print(substrings)
#


##### Second way by using comprehension ######

first_sequence = input().split(", ")
second_sequence = input().split(", ")
substring = [word for word in first_sequence if any(word in other_word for other_word in second_sequence)]
print(substring)