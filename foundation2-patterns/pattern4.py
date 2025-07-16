n = 5

for i in range(n, 0, -1):
    for j in range(n, 0, -1):
        if i>=j:
            # print(i, j, end="")
            print("*" ,end=" ")
        else:
            print(end="  ")
    print()