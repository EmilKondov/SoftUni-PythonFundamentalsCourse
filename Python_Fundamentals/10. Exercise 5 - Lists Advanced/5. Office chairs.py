def check_the_rooms(rooms):
    total_free_chairs = 0.
    total_needed_chairs = 0
    for room in range(1, rooms + 1):
        free_chairs_current_room, visitors = input().split()
        difference = len(free_chairs_current_room) - int(visitors)
        if difference < 0:
            print(f"{abs(difference)} more chairs needed in room {room}")
            total_needed_chairs += abs(difference)
        else: # difference >= 0:
            total_free_chairs += difference


    return total_free_chairs, total_needed_chairs




number_of_rooms = int(input())
total_free_chairs, total_needed_chairs = check_the_rooms(number_of_rooms)
if total_free_chairs >= total_needed_chairs:
    print(f"Game On, {total_free_chairs:.0f} free chairs left")
