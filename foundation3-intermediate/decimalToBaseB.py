temp = num = 634
b = int(input("Enter the base to convert to into:\n"))

baseNum = 0
x = 0

while not temp==0:
    q = temp%b
    
    baseNum += q*(10**x)
    x+=1
    temp//=b

print(baseNum)