capacity1 = int(input())
capacity2 = int(input())
capacity3 = int(input())
count_students = int(input())

total_capacity_hour = capacity1 + capacity2 + capacity3
time_needed = 0

while count_students > 0:
     time_needed+=1
     if time_needed % 4 == 0:
         continue
     count_students -= total_capacity_hour
print(f"Time needed: {time_needed}h.")



##Input
#
#capacity1 = int(input())
#capacity2 = int(input())
#capacity3 = int(input())
#count_students = int(input())
#
#total_capacity_hour = capacity1 + capacity2 + capacity3
#needed_time = 0
#
#students_counter = 0
#for students in range(1, count_students + 1):
#    students_counter +=1
#    count_students -= 1
#    if needed_time % 4 == 0 and needed_time != 0:
#        needed_time += 1
#    if students_counter == total_capacity_hour or count_students <= 0:
#        needed_time +=1
#print(f"Time needed: {needed_time}h.")
#