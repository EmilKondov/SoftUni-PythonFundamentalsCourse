main_stack = []

for _ in range(int(input())):
    numbers_data = input().split()
    action_code = numbers_data[0]

    if action_code == "1":
        main_stack.append(numbers_data[1])
    elif action_code == "2":
        if main_stack:
            main_stack.pop()
    elif action_code == "3":
        if main_stack:
            print(max(main_stack))
    elif action_code == "4":
        if main_stack:
            print(min(main_stack))

main_stack.reverse()

print(*main_stack, sep=", ")