import math

number_of_people = int(input())
cpacity_of_elevator = int(input())

courses = math.ceil(number_of_people / cpacity_of_elevator)

print(courses)