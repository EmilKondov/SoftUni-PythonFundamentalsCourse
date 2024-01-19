rows, columns = [int(x) for x in input().split()]

matrix = []

for row in range(rows):
    current_row = [x for x in input().split()]
    matrix.append(current_row)

sub_matrix = []
identical_squares_counter = 0


for row in range(rows -1):
    for col in range(columns -1):
        first_element = matrix[row][col]
        second_element = matrix[row][col + 1]
        third_element = matrix[row +1][col]
        fourth_element = matrix[row+1][col +1]

        sub_matrix = first_element, second_element, third_element, fourth_element

        if sub_matrix.count(sub_matrix[0]) == len(sub_matrix):
            identical_squares_counter += 1

print(identical_squares_counter)
