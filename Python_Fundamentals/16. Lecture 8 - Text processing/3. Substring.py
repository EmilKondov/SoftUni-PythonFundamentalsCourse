to_be_removed = input()
text_to_be_edited = input()

while to_be_removed in text_to_be_edited:
    text_to_be_edited = text_to_be_edited.replace(to_be_removed, "")
print(text_to_be_edited)
