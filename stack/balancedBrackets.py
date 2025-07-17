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
trueLine = "{[2x + 3(y - 4)] + (5z - {7x + 2})}"
falseLine = "{(3x + 5] - [2y - (4z + 1))}"

def isBalanced(string, stk):
    length = len(string)

    for i in range(0, length):
        # print(stk)
        ch = string[i]
        # print("ch", ch)
        if ch == ")":
            while not stk.peek() == "(":
                if stk.peek()=="[" or stk.peek()=="{":
                    return False
                else:
                    stk.pop()
            stk.pop()
        elif ch == "]":
            while not stk.peek() == "[":
                if stk.peek()=="(" or stk.peek()=="{":
                    return False
                else:
                    stk.pop()
            stk.pop()
        elif ch == "}":
            while not stk.peek() == "{":
                if stk.peek()=="(" or stk.peek()=="[":
                    return False
                else:
                    stk.pop()
            stk.pop()
        else:
            stk.push(ch)
        
    return True

print(isBalanced(trueLine, stack))
print(isBalanced(falseLine, stack))