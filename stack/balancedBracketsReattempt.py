e1 = "[(a + b) * {c - d + (e * f)] + g - h"
e2 = "x + y) - [z * (p + q}) + r)"
e3 = "{(m + n) * [o - p / (q + r)] + s}"
e4 = "({a - [b + (c * d)] + e * f) + g}"
e5 = "[x * (y + {z - w)] + (u / v}"

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



def isBalanced(string):
    stack = Stack()
    length = len(string)
    flag = True
    for i in range(0, length):
        ch = string[i]

        if ch=="(" or ch=="[" or ch=="{":
            stack.push(ch)
            continue

        if ch==")" and not stack.size()==0:
            if stack.peek() == "(":
                stack.pop()
            else:
                # print(stack)
                flag = False
        elif ch == "}" and not stack.size() == 0:
            if stack.peek() == "{":
                stack.pop()
            else:
                # print(stack)
                flag = False

        elif ch == "]" and not stack.size() == 0:
            if stack.peek() == "[":
                stack.pop()
            else:
                #print(stack)
                flag = False
       
    if not stack.size() == 0:
        # print(stack)
        flag = False 
    
    return flag

print(isBalanced(e1))
print(isBalanced(e2))
print(isBalanced(e3))
print(isBalanced(e4))
print(isBalanced(e5))