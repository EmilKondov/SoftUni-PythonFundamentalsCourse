def age_assignment(*names, **age_data):
    list = []

    for name, age in age_data.items():
        for current_name in names:
            if current_name.startswith(name):
                list.append(f"{current_name} is {age} years old.")
                break
    return "\n".join(sorted(list))


print(age_assignment("Peter", "George", G=26, P=19))

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))