# n = int(input("Enter number for the pattern:\n"))
n=5
print("-----------------------------------------------------------------")
for i in range(1, n+1):
    for j in range(1, n+1):
        if j<=i:
            print(j,"\t", end="")
        else:
           print("\t", end="")    
            
    for j in range(n-1, 0, -1):
        if j<=i:
            print(j, "\t", end="")
        else:
            print("\t", end="") 
    print()

print("-----------------------------------------------------------------")