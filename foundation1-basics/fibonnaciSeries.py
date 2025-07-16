n = int(input("Enter the number you want your fibonnaci series till:"))

a = 0
b = 1
print(a,b, end=" ")

for i in range(1, n+1):
    c = b + a
    a = b
    b = c
    print(c, end=" ")