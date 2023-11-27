


### Wrong interpretation of the conditions of this task ###
#numbers = input().split()
#numbers = [int(x) for x in numbers]       # Convert strings to integers
#numbers.sort(reverse=True)
#number_n = int(input())
#
#for number in range(len(numbers) - 1, -1, -1):
#    numbers.pop()
#    number_n -= 1
#    if number_n == 0:
#        break
#print(numbers)

#There are a couple of issues in your code. Let's address them:
 #In the for loop, you are trying to iterate over the numbers list using range(numbers, -1, -1). However, the range() function expects integer arguments, and you are passing a list. You should use range(len(numbers)-1, -1, -1) to iterate over the indices of the list in reverse order.
# When using numbers.remove(number) inside the loop, it modifies the list while you're iterating over it. This can lead to unexpected behavior. It's generally not recommended to modify a list while iterating over it. You can create a new list or use list comprehension to filter out the numbers you want to remove.
 #Here's a corrected version of your code:



### Correct solution ###

