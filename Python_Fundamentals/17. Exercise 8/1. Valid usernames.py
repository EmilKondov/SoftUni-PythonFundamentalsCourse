usernames = input().split(", ")
allowed_symbols = ["-", "_"]
valid_usernames = []
for name in usernames:
    name.strip()
    if 3 <= len(name) <= 16:
        if name.isalnum() or allowed_symbols[0] in name or allowed_symbols[1] in name:
            print(name)
            