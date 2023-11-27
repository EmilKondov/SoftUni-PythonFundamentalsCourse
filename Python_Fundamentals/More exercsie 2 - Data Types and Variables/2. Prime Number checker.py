given_number = int(input())

if given_number == 1:
    print("False")
elif given_number > 1:
    for i in range(2, given_number):
        if given_number % i == 0:
            print("False")
            break
    else:
        print("True")
