#                                                             My attempt
# n = 5

# for i in range(n//2+1, 0, -1):
#     print(" "*(n//2-1), end="")
#     for j in range(1, n//2+1):
#         if i<=j:
#             # print(i, j, end="")
#             print("*" ,end=" ")
#         else:
#             print(end=" ")
#     print()

# print("* "*(n//2+1))

# for i in range(1, n//2+1):
#     print(" "*(n//2-1), end="")
#     for j in range(1, n//2+1):
#         if i<=j:
#             # print(i, j, end="")
#             print("*" ,end=" ")
#         else:
#             print(end=" ")
#     print()

#                                             Retry after watching solution

n = 5
sp = n//2
st = 1

for i in range(1, n+1):
    for j in range(1, sp+1):
        print(" \t", end="")
        
    for j in range(1, st+1):
        print("* \t", end="")
    
    if i <= n//2:
        sp -=1
        st +=2
    else:
        sp +=1
        st -=2
    print()