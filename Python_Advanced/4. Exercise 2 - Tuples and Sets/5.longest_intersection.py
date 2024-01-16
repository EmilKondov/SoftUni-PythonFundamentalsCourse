# number_of_lines = int(input())
#
# intersections = []
# final_intersection = []
#
# for given_range in range(number_of_lines):
#     list_of_ranges = [[int(x) for x in x.split(',')] for x in input().split('-')]
#
#     current_set1 = {int(x) for x in range(list_of_ranges[0][0], list_of_ranges[0][-1] + 1)}
#     current_set2 = {int(x) for x in range(list_of_ranges[1][0], list_of_ranges[1][-1] + 1)}
#
#     current_intersection = list(current_set1 & current_set2)
#     intersections.append(len(current_intersection))
#
#     if len(current_intersection) > len(final_intersection):
#         final_intersection = current_intersection
#
# print(f"Longest intersection is {final_intersection} with length {max(intersections)}")

### Second solution ###
longest_intersection = set()

for _ in range(int(input())):
    first_range, second_range = [el.split(",") for el in input().split("-")]

    first_set = set(range(int(first_range[0]), int(first_range[-1]) + 1))
    second_set = set(range(int(second_range[0]), int(second_range[-1]) + 1))

    intersection = first_set.intersection(second_set)

    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(f"Longest intersection is [{', '.join(str(x) for x in longest_intersection)}] with length {len(longest_intersection)}")

