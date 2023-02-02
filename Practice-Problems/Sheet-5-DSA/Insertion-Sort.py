# Write a python program for Insertion  sort using  function.

def insertionSort(lst):
    for i in range(1,len(lst)):
        key=lst[i]
        j=i-1
        while(key<lst[j] and j>=0):
            lst[j+1]=lst[j]
            j-=1
        lst[j+1]=key
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
# for i in insertionSort(newList):
#     print(i,end="  ")
print(insertionSort(newList))