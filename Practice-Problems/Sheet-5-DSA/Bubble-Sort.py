# Write a python program for Bubble sort using  function.

def bubbleSort(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-1):
            if(lst[j]>lst[j+1]):
                temp = lst[j]
                lst[j]=lst[j+1]
                lst[j+1]=temp
    return lst

newList = []
n=int(input("Enter the number of Values you want : "))
for i in range(n):
    x = int(input(f"Enter {i+1} element : "))
    newList.append(x)
print("\nGiven list is",end=" ")
for i in newList:
    print(i,end="  ")
print("\nAscending order sorted list is",end=" ")
for i in bubbleSort(newList):
    print(i,end="  ")