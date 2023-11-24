def password_validator(password):
    is_valid = True
    if len(password) < 6 or len(password) > 10:
        print("Password must be between 6 and 10 characters")
        is_valid = False
    if not password.isalnum():
        print("Password must consist only of letters and digits")
        is_valid = False
    digits_counter = 0
    for character in password:
        if character.isdigit():
            digits_counter += 1
    if digits_counter < 2:
        print("Password must have at least 2 digits")
        is_valid = False
    return is_valid

password_input = input()
password_is_valid = password_validator(password_input)
if password_is_valid:
        print("Password is valid")
