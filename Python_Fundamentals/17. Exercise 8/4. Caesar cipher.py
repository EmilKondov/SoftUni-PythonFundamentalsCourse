text = input()
encrypted_text = []
for ch in range(len(text)):
    encrypted_text.append(chr(ord(text[ch]) + 3))
print("".join(encrypted_text))
