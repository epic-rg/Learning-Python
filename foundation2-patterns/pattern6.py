n = 5

st = n//2+1
sp = 1

for i in range(1, n+1):
    #first star
    for j in range(1, st+1):
        print("*\t", end="")
        
    #space
    for j in range(1, sp+1):
        print("\t", end="")
    
    #star
    for j in range(1, st+1):
        print("*\t", end="")
          
    # print(st, sp, st)
          
    if i < n//2+1:
        st-=1
        sp+=2
    else:
        st+=1
        sp-=2
    print()