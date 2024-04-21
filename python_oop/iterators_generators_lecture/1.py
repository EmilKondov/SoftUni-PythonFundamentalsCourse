class CustomRange():
    def __init__(self, start: int, end: int):
        self.i = start
        self.n = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.i <= self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration


one_to_ten = CustomRange(1, 10)

for num in one_to_ten:
    print(num)