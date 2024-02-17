from collections import deque

vowels = deque(input().split())
consonants = input().split()

words = {'rose': 'rose', 'tulip': 'tulip', 'lotus': 'lotus', 'daffodil': 'daffodil'}

while vowels and consonants:
    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()

    for word in words:
        words[word] = words[word].replace(current_vowel, '')
        words[word] = words[word].replace(current_consonant, '')

        if not words[word]:
            print(f"Word found: {word}")
            break
    else:
        continue

    break

else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")

if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
