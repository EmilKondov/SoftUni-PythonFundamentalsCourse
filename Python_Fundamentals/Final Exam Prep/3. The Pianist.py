def composer(number_of_pieces):
    composer_dictionary = {}


initial_input = int(input())

while True:
    command = input().split("|")
    if command[0] == "Stop":
        print(f"{Piece} -> Composer: {composer}, Key: {key}")
        break
    elif command[0] == "Add":
        pass
    elif command[0] == "Remove":
        pass
    elif command[0] == "ChangeKey":
        pass
