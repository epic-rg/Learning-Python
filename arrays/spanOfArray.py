n = int(input("Enter the size of array"))

array = []


for i in range(1, n):
    x = int(input("Enter:"))
    array.append(x)

max = min = array[0]

for arr in array:
    if arr > max:
        max = arr
    
    if arr < min:
        min = arr
        
print(f"The span of this array is {max - min}")