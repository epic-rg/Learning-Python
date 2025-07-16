n = 5

inSpace = -1
outSpace = n//2

for i in range(1, n+1):
    # print(outSpace, inSpace)

    for j in range(1, outSpace+1):
        print("\t", end="")

    print("*\t", end="")

    for j in range(1, inSpace+1):
        print("\t", end="")
        
    if(not inSpace==-1):
        print("*\t", end="")

    if i <= n//2:
        inSpace += 2
        outSpace -=1
    else:
        inSpace -=2
        outSpace+=1
    print()