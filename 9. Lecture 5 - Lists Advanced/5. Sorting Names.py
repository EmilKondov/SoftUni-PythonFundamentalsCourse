given_names = input().split(", ")

sorted_names = sorted(given_names, key=lambda x: (-len(x), x))
print(sorted_names)
