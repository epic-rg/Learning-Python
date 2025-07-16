n = 6

list = []

for i in range(1, n):
    list.append(input("Enter"))

item = input("Enter the item for Searching:")


def linearSearch(_list, _item):
    size = len(list)
    for i in range(0, size):
        if _list[i] == _item:
            return i
    return -1

flag = linearSearch(list, item)

if flag==-1:
    print("The item in not present in the list.")
else:
    print(f"The item is present on the index: {flag}")