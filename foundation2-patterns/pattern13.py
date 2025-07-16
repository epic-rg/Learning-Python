n = 7

for i in range(0, n):
    icj = 1
    for j in range(0, i+1):
        print(f"{icj}\t", end='')
        icjp1 = int(icj * (i-j) )/(j+1)
        icj = int(icjp1)
    print()