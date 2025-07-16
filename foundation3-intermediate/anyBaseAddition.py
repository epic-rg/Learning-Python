num1 = 1234
num2 = 3
base = 5

sum = 0
x = 0
c = 0 

while not num1==0:
    q1 = num1%10
    q2 = num2%10
    
    # print("qs", q1, q2)
    
    s = q1+q2+c
    c = 1 if s//base > 0 else 0
    s = s%base
    
    print("cs", c, s)
    sum += s * (10**x) 
    x+=1
    
    num1//=10
    num2//=10

if c == 1:
    sum += c * (10**(x))
 
print(sum)