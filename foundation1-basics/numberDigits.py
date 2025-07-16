import math

x = int(input("Enter a number:"))

def numCount(n):
    count = 0

    while not n == 0:
      n//=10
      count += 1
    
    return count 


def printNums(n):
    div = int(math.pow(10, numCount(n) - 1))
    while not n == 0:
        q = n // div
        print(q)

        n %= div
        div //= 10

printNums(x)