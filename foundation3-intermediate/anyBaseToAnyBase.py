num = 1172
b1 = 8
b2 = 2

decimalNum = 0
x = 0

def deciToAnyBase(num, base):
    baseNum = 0
    x = 0

    while not num==0:
        q = num%base
        
        baseNum += q*(10**x)
        x+=1
        num//=base

    return baseNum  

def anyBaseToDecimal(num, base):
    decimalNum = 0
    x = 0
    
    while not num ==0:
        q = num%10
        decimalNum += q * base**x
        x+=1
        num //= 10
    return decimalNum

finalNum = deciToAnyBase(anyBaseToDecimal(num, b1), b2)
print(finalNum)