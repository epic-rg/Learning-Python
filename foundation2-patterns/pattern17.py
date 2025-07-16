n =5

sp = n//2
st = 1

for i in range(1, n+1):
    for j in range(1, sp+1):
        print("\t", end="")
    for j in range(1, st+1):
        if not j<=st//2 or i==n//2+1:
            print("*\t", end="")
        else:
            print("\t", end="")

    if i <= n//2:
        sp-=1
        st+=2
    else:
        sp+=1
        st-=2
    print()