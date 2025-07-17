num1 = [9, 8, 9]
num2 = [2, 8]

len1 = len(num1)
len2 = len(num2)

finalNum = []
carry = 0
i = len1 -1
j = len2 - 1

k = i if i>j else j

while k>=0:
    temp = carry
    if i>=0:
        temp += num1[i]
    if j>=0:
         temp += num2[j]

    carry = temp // 10
    temp %= 10
    
    finalNum.insert(0, temp)
    
    i-=1 
    j-=1
    k-=1 
    
if carry != 0:
    print(carry, end="")

for item in finalNum:
    print(item, end="")