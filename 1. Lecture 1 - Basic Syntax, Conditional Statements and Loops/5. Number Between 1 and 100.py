#floating_point_number = float(input())
#for i in range(1, 101):
#    number = float(input())
#    if number > 1 and number <= 100:
#        print(f"The number {number:.1f} is between 1 and 100")
#

number = float(input())
while number < 1 or number > 100:
    number = float(input())
print(f"The number {number} is between 1 and 100")
