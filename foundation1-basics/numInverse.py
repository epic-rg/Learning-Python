import math
# num = int(input("Enter a number:\n"))
num = 3241576

def numCount(n):
    count = 0

    while not n == 0:
      n//=10
      count += 1
    
    return count 

len = numCount(num)

flag = True

for i in range(1,len+1):
    temp = num
    count = 0
    # print(i)
    while not temp == 0:
        q = temp%10
        # print(f"q {q}")
        # print(f"i {i}")
        if q==i:
            count += 1
        temp//=10
    # print("----------------------------")
    # print(f"{count} count")
    if not count==1:
        flag = False
        
# print(flag)



def inverse(temp):
    inverseNum = 0
    for i in range(1, len+1):
        q = temp%10
        inverseNum += int(math.pow(10, q-1) * i)
        temp//=10
    return inverseNum

if flag:
    print(f"{inverse(num)} if the inverse Number for {num}")
else:
    print(f"{num} is a not a valid Number.")