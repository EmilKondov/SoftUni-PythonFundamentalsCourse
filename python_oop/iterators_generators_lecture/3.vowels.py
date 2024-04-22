class vowels:
    def __init__(self, obj_iterable):
        self.obj_iterable = obj_iterable
        self.vowels_list = ["a", "e", "i", "u", "o", "y"]
        self.index = -1
        self.iterable_list = [c for c in self.obj_iterable if c.lower() in self.vowels_list]

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index < len(self.iterable_list):
            return self.iterable_list[self.index]
        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)