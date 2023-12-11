words = ["Sand", "Water", "Fish", "Sun"]
entry_word = input().lower()
counter = 0

for word in words:
    word = word.lower()
    if word in entry_word:
        counter += 1
print(counter)