number_of_electrons = int(input())

filled_shells = []


for n in range(1, number_of_electrons +1):
    if number_of_electrons > 0:
        max_electrons_in_shell = 2 * n **2
        if max_electrons_in_shell > number_of_electrons:
            filled_shells.append(number_of_electrons)
            break
        number_of_electrons -= max_electrons_in_shell
        filled_shells.append(max_electrons_in_shell)
print(filled_shells)
