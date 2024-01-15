number_of_lines = int(input())

intersections = []
collection_of_intersections = {}

for given_range in range(number_of_lines):
    list_of_ranges = [[int(x) for x in x.split(',')] for x in input().split('-')]

    current_set1 = {int(x) for x in range(list_of_ranges[0][0], list_of_ranges[0][-1] + 1)}
    current_set2 = {int(x) for x in range(list_of_ranges[1][0], list_of_ranges[1][-1] + 1)}

    intersections.append(len(current_set1 & current_set2))

    if len(current_set1.intersection(current_set2)) > int(intersections[given_range -1]):
        final_intersection = list(current_set1 & current_set2)

print(f"Longest intersection is {final_intersection} with length {max(intersections)}")
