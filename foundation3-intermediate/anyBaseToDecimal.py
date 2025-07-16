temp = num = 1172
b = 8

decimalNum = 0
x = 0

while not temp ==0:
    q = temp%10
    decimalNum += q * b**x
    x+=1
    temp //= 10

print(decimalNum)