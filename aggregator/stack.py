
class StackIsEmpty(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message


class Stack:
    def __init__(self, data=None):
        if data is None:
            self._data = []
        else:
            self._data = list(data)

    def __len__(self):
        return len(self._data)

    def __str__(self):
        stackStr = ', '.join(str(x) for x in self._data)
        return f'Stack({stackStr})'

    def __repr__(self):
        stackStr = ', '.join(repr(x) for x in self._data)
        return f'Stack([{stackStr}])'

    def peek(self):
        if len(self) == 0:
            raise StackIsEmpty("Stack is empty!")
        return self._data[-1]

    def push(self, val):
        self._data.append(val)

    def pop(self):
        if len(self) == 0:
            raise StackIsEmpty("Stack is empty!")
        return self._data.pop()

    def __enter__(self):
        self._len_at_enter = len(self)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        while len(self) > self._len_at_enter:
            self.pop()
        return False
