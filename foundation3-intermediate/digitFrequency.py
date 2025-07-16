n = int(input("Enter a number:\n"))
x = int(input("Enter a the digit to check frequency for:\n"))

def frequency(a, b):
    count = 0
    while not a==0:
        q = a%10
        if q == b:
            count +=1
        a//=10
    return count

print(f"The frequency of {x} in {n} is {frequency(n, x)}.")        