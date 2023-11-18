given_number_n = int(input())
given_word = input()

text_list = []
text_list_filtered = []

for current_text in range(given_number_n):
    current_text = input()
    text_list.append(current_text)
    if given_word in current_text:
        text_list_filtered.append(current_text)


print(text_list)
print(text_list_filtered)
