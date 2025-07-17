from collections import deque

class Stack:
    def __init__(self):
        self._container = deque()

    def push(self, item):
        self._container.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self._container.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self._container[-1]

    def is_empty(self):
        return not self._container

    def size(self):
        return len(self._container)

    def __repr__(self):
        return f"Stack({list(self._container)})"


stack = Stack()
falseLine = "(a + b) - (2a + 8)"
trueLine = "(x+y) - ((x-y))"

def isDuplicate(string, deStack):
    length = len(string)

    for i in range(0, length):
        ch = string[i]
        print("ch", ch)
        if ch == ")":
            if deStack.peek()=="(":
                return True
            else:
                while not deStack.peek() == "(":
                    deStack.pop()
                deStack.pop()
        else:
            deStack.push(ch)
        
    return False


print(isDuplicate(falseLine, stack))