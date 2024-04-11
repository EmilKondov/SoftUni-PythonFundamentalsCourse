def decrypt_message(stops):

    while True:
        command = input()
        initial_string = stops

        if command.startswith("Travel"):
            print(f"Ready for world tour! Planned stops: {stops}")
            break


        elif command.startswith("Add"):
            current_command, index, string = command.split(":")
            if 0 < int(index) < len(stops):
                stops = stops[:int(index)] + string + stops[int(index):]
                print(stops)
            else:
                print(stops)


        elif command.startswith("Remove"):
            current_command, start_index, end_index = command.split(":")
            if 0 < int(start_index) < len(stops) and 0 < int(end_index) < len(stops):
                stops = stops[: int(start_index)] + stops[int(end_index) + 1:]
                print(stops)
            else:
                print(stops)

        elif command.startswith("Switch"):
            current_command, old_string, new_string = command.split(":")
            if old_string in initial_string:
                stops = stops.replace(old_string, new_string)
                print(stops)
            else:
                print(stops)

data = input()
decrypt_message(data)

