n = 7

sp = 0
st = n

for i in range(1, n+1):
    for j in range(0, sp):
        print("\t", end="")
    
    for j in range(1, st+1):
        if (i<=n//2 and not i==1) and (j<st and not j==1):
            print("\t", end="")
        else:
            print("*\t", end="")

    if i <= n//2:
        sp+=1
        st-=2
    else:
        sp-=1
        st+=2
    print()