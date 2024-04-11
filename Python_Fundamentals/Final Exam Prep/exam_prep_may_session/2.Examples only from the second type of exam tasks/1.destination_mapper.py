import re

def valid_destination_function(destination_data):

    pattern = r"(\=|\/)([A-Z][A-Za-z]{2,})\1"
    travel_points = 0
    valid_destinations = []
    result = re.finditer((pattern, destination_data))

    for current_destination in result:
        valid_destinations.append(current_destination.group(2))


data = input()
valid_destination_function(data)