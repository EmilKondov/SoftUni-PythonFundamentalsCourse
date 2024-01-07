text = input()
emoticon_always_start_with = ":"

for ch in range(len(text)):
    if ":" in text[ch]:
        emoticon = text[ch + 1]
        print(f":{emoticon}")

