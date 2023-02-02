# Write a python program for Selection  sort using  function.

def min(lst):
    minEle = lst[0]
    for i in range(len(lst)):
        if (minEle >= lst[i]):
            minEle = lst[i]
            pos = i
    return pos


def selectionSort(lst):
    for i in range(len(lst)):
        minEle = i + min(lst[i:])
        # swap(lst[i],lst[minEle])
        temp = lst[i]
        lst[i] = lst[minEle]
        lst[minEle] = temp
    return lst


newList = []
n = int(input("Enter the number of Values you want : "))
for i in range(n):
    x = int(input(f"Enter {i+1} element : "))
    newList.append(x)
print("\nGiven list is",end=" ")
for i in newList:
    print(i,end="  ")
print("\nAscending order sorted list is",end=" ")
for i in selectionSort(newList):
    print(i,end="  ")