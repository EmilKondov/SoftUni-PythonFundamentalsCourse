def chairs(some_number):
    total_free_chairs = 0
    for room in range(1, some_number + 1):
        free_chairs, people  = input().split()
        difference = len(free_chairs) - int(people)
        if difference < 0:
            print(f"{abs(difference)} more chairs needed in room {room}")
        else: # meaning difference >= 0
            total_free_chairs += difference
            print(f"Game On, {total_free_chairs} free chairs left")
    return total_free_chairs




number_of_rooms = int(input())
chairs(number_of_rooms)