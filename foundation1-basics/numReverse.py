x = int(input("Enter a number:\n"))

rev = 0
temp = x

while not temp==0:
    q = temp % 10
    rev = rev*10 + q
    
    temp //= 10
    
print(rev)