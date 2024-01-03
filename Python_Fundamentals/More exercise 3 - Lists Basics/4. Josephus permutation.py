people = input().split()
k_skip = int(input())

k_skip -= 1
executed_people = []
index = k_skip % len(people)

while len(people) > 1:
    executed_people.append(people.pop(index))
    index = (index + k_skip) % len(people)

executed_people.append(people[0])
print((str(executed_people).replace(' ', '').replace('\'', '')))
