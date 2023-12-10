def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        middle_index = left + right // 2
        middle_element = numbers[middle_index]

        if target == middle_element:
            return middle_element

        if  target < middle_element:
            right = middle_index - 1

        else:
            left = middle_index + 1

nums = [int(i) for i in input().split()]
target = int(input("Target numbers is:"))
print(binary_search(nums, target))