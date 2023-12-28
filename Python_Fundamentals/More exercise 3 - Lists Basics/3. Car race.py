def left_racer(times, finish_index):
    total_time_one = 0
    for i in range(finish_index):
        time = times[i]
        if time == 0:
            total_time_one -= total_time_one * 0.20
        total_time_one += time
    return total_time_one

def right_racer(times, finish_index):
    total_time_two = 0
    for i in range(len(times) -1, finish_index, -1):
        time = times[i]
        if time == 0:
            total_time_two -= total_time_two * 0.20
        total_time_two += time
    return total_time_two



list_of_times = [int(x) for x in input().split()]
finish_line_index = len(list_of_times) // 2
racer_one = left_racer(list_of_times, finish_line_index)
racer_two = right_racer(list_of_times, finish_line_index)

if racer_one < racer_two:
    print(f"The winner is left with total time: {racer_one}")
else:
    print(f"The winner is right with total time: {racer_two}")
