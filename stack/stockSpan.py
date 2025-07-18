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

newList = [2, 5, 9, 3, 1, 12, 6, 8, 7]

answer = [1, 2, 3, 1, 1, 6, 1, 2, 1 ]
length = len(newList)

solve = []
# stack.push(newList[0])
for i in range(length):
    while stack.size() > 0 and newList[stack.peek()] < newList[i]:
       stack.pop()
    
    if stack.size() == 0: 
        solve.append(i+1)
    else:
        solve.append(i - stack.peek())
    stack.push(i)

print(solve)