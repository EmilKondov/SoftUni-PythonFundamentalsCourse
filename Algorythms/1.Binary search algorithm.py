def binary_search(num, target):
    low = 0
    high = len(num)
    while low < high:
        mid_index = (low + high) // 2
        mid_element = num[mid_index]

        if mid_element < target:
            low = mid_index + 1
        elif mid_element > target:
            high = mid_index
        else:
            mid_element == target
            print("Here is the index of the number you look for:", end="")
            return mid_index
    return "Target is out of the range. Please enter another number"

numbers = [x for x in range(int(input()))]
target_number = int(input("Enter the number you are looking for: "))
print(binary_search(numbers, target_number))