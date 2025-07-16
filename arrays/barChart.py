n = 6
list = [2, 4, 7, 5, 0, 9]

max = list[0]

for item in list:
    if item > max:
        max = item
        
for floor in range(max, 0, -1):
    for i in range(0, n):
        if floor <= list[i]:
            print("*\t", end="")
        else:
            print("\t", end="")
    print()