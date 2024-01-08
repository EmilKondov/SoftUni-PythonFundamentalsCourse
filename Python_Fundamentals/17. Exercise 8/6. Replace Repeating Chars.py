given_string = input()
final_text = ""
last_character = ""


for ch in given_string:
    current_character = ch
    if current_character in given_string:
        if ch != last_character:
            final_text += ch
            last_character = current_character
        else:
            continue
print(final_text)
