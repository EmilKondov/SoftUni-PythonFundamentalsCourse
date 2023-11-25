vowels = input()
sorted_vowels = [letter for letter in vowels if letter.lower() not in ['a', 'o', 'u', 'e', 'i']]

print(''.join(sorted_vowels))
