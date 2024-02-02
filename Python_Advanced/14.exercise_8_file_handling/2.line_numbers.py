from string import punctuation

with open("files/text2.txt", "r") as text_file:
    text = text_file.readlines()

output_file = open("files/text2_new.txt", "w")

for row in range(len(text)):
    characters, symbols = 0, 0

    for symbol in text[row]:
        if symbol.isalpha():
            characters += 1
        elif symbol in punctuation:
            symbols += 1

    output_file.write(f"Line {row + 1}: {''.join(text[row][:-1])} ({characters})({symbols})\n")
output_file.close()