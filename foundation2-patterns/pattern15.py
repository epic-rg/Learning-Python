n = 5

sp = n//2
st = 1

x=1

for i in range(1, n+1):
    for j in range(1, sp+1):
        print("\t", end="")
        
    cx = x
    for j in range(1, st+1):
        print(f"{cx}\t", end="")
        if j<=st//2:
            cx+=1
        else:
            cx-=1

    if i <= n//2:
        sp-=1
        st+=2
        x+=1
    else:
        sp+=1
        st-=2
        x-=1
    print()