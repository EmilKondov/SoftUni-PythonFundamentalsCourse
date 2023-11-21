numbers = input().split()
numbers.sort()
numbers.sort(reverse=True)

number_n = int(input())

for number in numbers:
    numbers.remove(number)
    number_n -= 1
    if number_n == 0:
        break
print(numbers.sort())
