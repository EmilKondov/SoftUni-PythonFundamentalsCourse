def find_the_sum(nums, idx=0):
    if idx == len(nums) - 1:
        return nums[idx]
    return nums[idx] + find_the_sum(nums, idx + 1)

nums = [int(x) for x in input().split()]
print(find_the_sum(nums))
