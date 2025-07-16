import math

n = 918624
k = -3

shift_var = 0


no_digit = 0
temp = n
while not temp == 0:
    no_digit += 1
    temp//=10

if k>0 and k<no_digit:
    shift_var = k
elif k>0 and k>no_digit:
    shift_var = k%no_digit
elif k<0 and abs(k)<no_digit:
    shift_var = no_digit+k
else:
    shift_var = no_digit+k

mul = math.pow(10, no_digit-shift_var)
div = math.pow(10, shift_var)

finalNum = int((n%div)*mul + n//div)
print(f"The final number after roatation is {finalNum}")