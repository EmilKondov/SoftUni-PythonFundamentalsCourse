list_words = input().split()
palindrome = input()

list_of_palindromes = []
number_of_repeated_palindromes = 0

for word in list_words:
    if word == word[::-1]:
        list_of_palindromes.append(word)
    if word == palindrome:
        number_of_repeated_palindromes += 1

print(list_of_palindromes)
print( f"Found palindrome {number_of_repeated_palindromes} times")
