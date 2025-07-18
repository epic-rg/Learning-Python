list = [2, 5, 9, 3, 1, 12, 6, 8, 7]

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
stack.push(0)
length = len(list)
solved = [-1] * length

# [5, 9, 12, 12, 12, -1, 8, -1, -1] answer for referance

for i in range(1, length):
    # print(list[stack.peek()])
    while stack.size() > 0 and list[i] >= list[stack.peek()]:
        print(list[i], list[stack.peek()])
        x = stack.pop()
        solved[x] = list[i]
        
    stack.push(i)

print(solved)