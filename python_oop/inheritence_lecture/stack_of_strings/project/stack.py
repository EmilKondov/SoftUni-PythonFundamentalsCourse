class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self) -> int:
        return self.data[-1]

    def is_empty(self) -> bool:
        return False if self.data else True

    def __str__(self):
        reversed_data = reversed(self.data)
        result = ", ".join(reversed_data)
        return f"[{result}]"
