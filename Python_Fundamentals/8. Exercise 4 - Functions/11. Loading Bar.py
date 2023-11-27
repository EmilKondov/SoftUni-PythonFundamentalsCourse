def loading_bar(some_number: int):
    if some_number == 100:
        return f'100% Complete!\n [%%%%%%%%%%]'
    return f'{some_number}% [{"%" * (some_number // 10)}{"." * (10-some_number//10)}]\n Still loading...'


given_number = int(input())
print(loading_bar(given_number))
