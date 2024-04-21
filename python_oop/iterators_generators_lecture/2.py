class ReverseIter():
    def __init__(self, iterable):
        self.iterable = iterable
        self.i = len(self.iterable) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.i > 0:
            i = self.i
            self.i += 1
            print(self.i)
            self.i -= 2
            return i
        else:
            raise StopIteration

reversed_list = ReverseIter([1, 2, 3, 4, 5, 6])
for item in reversed_list:
    print(item)