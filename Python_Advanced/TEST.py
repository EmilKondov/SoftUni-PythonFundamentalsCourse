# def palindrome(word, index):
#     if index == len(word) // 2:
#         return f"{word} is a palindrome"
#     if word[index] != word[-index -1]:
#         return f"{word} is not a palindrome"
#
#     return palindrome(word, index -1)
#
SIZE = 8

alphabet = ['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
chess_board = ''
chess_board_matrix = []

for char in alphabet:
    for num in range(1, SIZE + 1):
        chess_board += (f"{(char + str(num))} ")
    chess_board += "\n"

