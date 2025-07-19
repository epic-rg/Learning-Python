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

newList = [6, 2, 5, 4, 5, 1, 6]
length = len(newList)

maxArea = 0


#generates an array for the right boundary i.e. largest greatest on the right
rb = [length]
for i in range(length-2, -1, -1):
    while stack.size() > 0 and newList[stack.peek()] > newList[i]:
        stack.pop()
        
    if stack.size() == 0: 
        rb.insert(0, length)
    else:
        rb.insert(0, stack.peek())
        
    stack.push(i)

print(rb)

stack = Stack()
#generates an array for the left boundary i.e. largest greatest on the left
lb = [-1]
for i in range(1, length):
    while stack.size() > 0 and newList[stack.peek()] > newList[i]:
        stack.pop()
    
    if stack.size() == 0: 
        lb.append(-1)
    else:
        lb.append(stack.peek())

    stack.push(i)

print(lb)

for i in range(length):
    width = rb[i] - lb[i] - 1
    area = width*newList[i]

    if area > maxArea:
        maxArea = area

print(maxArea)