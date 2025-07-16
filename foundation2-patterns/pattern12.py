n = 5

a = 0 
b = 1

for i in range(1, n+1):
    for j in range(1, i+1):
        c = a+b
        print(a, "\t", end="")
        a = b
        b = c
    print()