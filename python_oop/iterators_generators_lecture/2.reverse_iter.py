class reverse_iter():
    def __init__(self, iterable):
        self.iterable = iterable
        self.start_index = 0
        self.end_index = len(self.iterable)
    """
    Here we have two options: 
    
    1. Is to use the next protocol which is an option inside 
    the list.
    
    2. Is to use separetley the __next__ protocol.
    """
    def __iter__(self):
        return reversed(self.iterable)

    # def __next__(self):
    #     self.end_index -= 1
    #     if self.end_index >= self.start_index:
    #         return self.iterable[self.end_index]
    #     raise StopIteration


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)