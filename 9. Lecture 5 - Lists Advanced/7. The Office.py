employees_happiness = input().split()
improvement_factor = int(input())

employees = list(map(lambda x: int(x) * improvement_factor, employees_happiness))
filtered_employees = filter(employees)

print(employees)