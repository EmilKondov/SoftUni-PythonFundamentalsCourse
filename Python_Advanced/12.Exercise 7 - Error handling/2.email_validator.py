class NameTooShortError(Exception):
    pass

class MustContainAtSymbolError(Exception):
    pass

class InvalidDomainError(Exception):
    pass

class MoreThanOneAtSymbol(Exception):
    pass


VALID_DOMAINS = ("com", "bg", "net", "org",)
MIN_LETTERS_IN_NAME = 4


user_input = input("Enter your e-mail here: ")

while user_input != "End":

    if "@" not in user_input:
        raise MustContainAtSymbolError("Email must contain @")
    elif user_input.count("@") > 1:
        raise MoreThanOneAtSymbol("There should be no more than one @ in your e-mail")
    elif user_input.split(".")[-1] not in VALID_DOMAINS:
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join('.' + d for d in VALID_DOMAINS)}")
    elif len(user_input.split("@")[0]) <= MIN_LETTERS_IN_NAME:
        raise NameTooShortError("Name must be more than 4 characters")

    print("Email is valid")

    user_input = input("Enter your e-mail here: ")

