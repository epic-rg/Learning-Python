num1 = 1212
num2 = 236
base = 8

neg = num1 < num2

if neg:
    temp = num1
    num1 = num2
    num2 = temp

sum = 0
x = 0
c = 0 

while not num1==0:
    q1 = num1%10
    q2 = num2%10
    
    # print("qs", q1, q2)
    q1-=c
    
    if q1 >= q2:
        s = q1-q2
        c=0
    else:
        q1+=base
        c=1
        s = q1-q2
    
    print("cs", c, s)
    sum += s * (10**x) 
    x+=1
    
    num1//=10
    num2//=10

if c == 1:
    sum += c * (10**(x))

if neg:
    sum *= -1
 
print(sum)