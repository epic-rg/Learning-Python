n = 5

for i in range(1, n+1):
    for j in range(1, n+1):
        if i==j or i==n-j+1:
            print("*\t", end="")
        else:
            print(" \t", end="")
    print()