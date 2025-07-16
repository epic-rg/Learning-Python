temp = num = 1440
i = 2

while not temp==1:
# for x in range(1, 50):
    # print("loop start")
    if temp%i==0:
        # print(temp)
        print(i, end=" ")
        temp//=i
    else:
        i += 1
    # print("-----------------")
print("Finished!")