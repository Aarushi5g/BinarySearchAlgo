def binary_search(list1, target1):
    lower = 0
    upper = len(list1) - 1
    while lower <= upper:
        mid = (upper + lower) // 2
        if list1[mid] < target1:
            lower = mid + 1
        elif list1[mid] > target1:
            upper = mid - 1
        else:
            return mid
    return -1


length = int(input("Enter the length of the list: "))
list1 = []
for i in range(0, length):
    element = int(input(f"Enter the element at the index {i}: "))
    list1.append(element)
list1.sort()
print(list1)
x = int(input("Enter the target value: "))
result = binary_search(list1, x)

if result != -1:
    print(f"Element is present at index {(result)} of the list {list1}")
else:
    print(f"Element is not present in the list {list1}")
