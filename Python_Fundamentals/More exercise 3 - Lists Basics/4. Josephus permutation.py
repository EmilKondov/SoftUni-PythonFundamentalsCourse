people = input().split()
k = int(input())

k -= 1
index = k % len(people)
killed = []

while len(people) > 1:
    killed.append(people.pop(index))
    index = (index + k) % len(people)
killed.append(people[0])

# result = "".join(killed).replace("", ",").strip(",")
# print(f"[{result}]")

### or

print(str(killed).replace(" ", "").replace("\'", ""))