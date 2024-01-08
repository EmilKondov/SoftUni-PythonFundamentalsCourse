given_string = input()
final_text = ""
last_character = ""

for ch in given_string:
    if ch != last_character:
        final_text += ch
        last_character = ch
    else:
        continue
print(final_text)
