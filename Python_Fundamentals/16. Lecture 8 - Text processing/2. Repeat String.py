given_strings = input().split()
final_string = ""

for word in given_strings:
    final_string += (word * len(word))
print(final_string)
