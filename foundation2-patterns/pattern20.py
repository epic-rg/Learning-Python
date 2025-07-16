n = 5

for i in range(1, n+1):
    for j in range(1, n+1):
        if j==1 or j==n:
            print("*\t", end="")
        else:
            if i>=n//2+1 and (i==j or i+j==n+1):
                print("*\t", end="")
            else:
                print("\t", end="")
    print()
    print()