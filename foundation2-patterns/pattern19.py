n = 7

for i in range(1, n+1):
    for j in range(1, n+1):
        # print("*\t", end="")
        
        if i ==1:
            if j <= n//2+1 or j==n:
                print("*\t", end="")
            else:
                print("\t", end="")
        elif i <= n//2:
            if j==n//2+1 or j==n:
                print("*\t", end="")
            else:
                print("\t", end="")
        elif i==n//2+1:
            print("*\t", end="")
        elif i < n:
            if j==n//2+1 or j==1:
                print("*\t", end="")
            else:
                print("\t", end="")
        else:
            if j >= n//2+1 or j==1:
                print("*\t", end="")
            else:
                print("\t", end="")
    print()
    print()