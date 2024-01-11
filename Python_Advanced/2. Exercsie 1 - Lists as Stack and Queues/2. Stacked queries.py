main_stack = []
track_stack = []
integer_n = int(input())

for query in range(integer_n):
    query = input().split()
    if len(query) == 1:
        action_code = query[0]
    elif len(query) > 1:
        action_code, value = query


    if action_code == "1":
        main_stack.append(value)
        if len(main_stack) == 1:
            track_stack.append(value)
        if main_stack[-1] > track_stack[-1]:
            track_stack.append(value)
        else:
            track_stack.append(track_stack[-1])
    elif action_code == "2":
        main_stack.pop()
        track_stack.pop()
    elif action_code == "3":
        print(max(main_stack))
        #print(track_stack[-1])
    elif action_code == "4":
        print(min(main_stack))
while main_stack:
    print(main_stack.pop(), end=" ")
