a = 5
b = 13 
c = 12

max = b1 = c1 = 0

if a>b and a>c:
    max = a
    b1 = b
    c1 = c
elif b>a and b>c:
    max = b
    b1 = a
    c1 = c
else:
    max = c
    b1 = b
    c1 = a

flag = max**2 == b1**2 + c1**2

if flag:
    print("Prime Triplet")
else:
    print("Not a prime triplet")