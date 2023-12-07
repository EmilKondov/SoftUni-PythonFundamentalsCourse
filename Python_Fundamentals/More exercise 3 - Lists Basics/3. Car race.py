list_of_times = input().split()

finish_line_index = len(list_of_times) // 2
total_time_left_racer = 0
total_time_right_racer = 0

while True:
    for left_time in list_of_times:
        total_time_left_racer += int(left_time)
        for right_time in range(len(list_of_times)-1, -1,- 1):
            total_time_right_racer += int(list_of_times[right_time])




print(finish_line_index)