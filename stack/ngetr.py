list = [2, 5, 9, 3, 1, 12, 6, 8, 7]
solve = [-1]

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

stack.push(list[len(list)-1])

for i in range(len(list)-2, -1, -1):
    while stack.size() > 0 and list[i] >= stack.peek():
        stack.pop()
        
    if stack.size() == 0:
        solve.insert(0, -1)
    else:
        solve.insert(0, stack.peek())
    
    stack.push(list[i])

print(solve)