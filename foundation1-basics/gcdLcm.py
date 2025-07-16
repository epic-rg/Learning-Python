num1 = 12
num2 = 8

gcd = lcm = min(num1, num2)

len = max(num1, num2)

while not (lcm%num1==0 and lcm%num2==0):
    # print(lcm)
    lcm += 1

print(lcm)

while not (num1%gcd==0 and num2%gcd==0):
    gcd -= 1
    
print(gcd)