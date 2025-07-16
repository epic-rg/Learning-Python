def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


a = int(input("Enter a range to check for prime numbers: ")) 

for i in range(2, a + 1):
    if is_prime(i):
        print(f"{i} is a prime number.")
    