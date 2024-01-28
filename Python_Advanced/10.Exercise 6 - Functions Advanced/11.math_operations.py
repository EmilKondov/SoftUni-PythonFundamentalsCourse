from collections import deque
#Logic
def math_operations(*numbers, **operations):
    numbers_collection = deque(numbers)
    while numbers_collection:                                            #Чрез popleft() премахваме един по един всеки елемент от numbers_collection въртейки цикъл през KVP на operations речника.
        for key, value in operations.items():
            if not numbers_collection:
                break
            if key == "a":
                operations[key] = (numbers_collection.popleft() + value)
            elif key == "s":
                operations[key] = (value - numbers_collection.popleft())
            elif key == "d":
                if numbers_collection[0] == 0:
                    numbers_collection.popleft()
                else:
                    operations[key] = (value / numbers_collection.popleft())
            elif key == "m":
                operations[key] = (numbers_collection.popleft() * value)
    else:
        sorted_collection = sorted(operations.items(), key = lambda x: (-x[1], x[0]))
        list_of_sorted_collection = []
        for key, value in sorted_collection:
            list_of_sorted_collection.append(f"{key}: {value:.1f}")
        return "\n".join(list_of_sorted_collection)
#print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
#print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))