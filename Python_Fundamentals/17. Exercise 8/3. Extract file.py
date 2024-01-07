path = input().split("\\")

for location in path:
    if "." in location:
        file_name, file_extension = location.split(".")
        print(f"File name: {file_name}\nFile extension: {file_extension}")
