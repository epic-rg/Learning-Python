n = int(input("Enter number of benjamin bulbs:\n"))

#In this program, the bulbs that are on are of prefect sqaures, since prime numbers have odd number of factors and rest doesn't have odd number of factors, therefor the only bulbs that are left turned on are of perfect squares

i = 1
while i**2<n:
    print(i**2)
    i+=1