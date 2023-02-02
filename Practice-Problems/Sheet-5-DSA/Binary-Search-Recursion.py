# Write a python program for  Binary Search using  recursive function.

def binary(lst,low,high,searchEle):
    mid=(low+high)//2
    if(low<=high):
        if(lst[mid]==searchEle):
            return mid+1
        elif(lst[mid]>searchEle):
            high=mid-1
        elif(lst[mid]<searchEle):
            low=mid+1
        return binary(lst,low,high,searchEle)
    return -1

newList = []
n=int(input("Enter the number of Values you want : "))
for i in range(n):
    x = int(input(f"Enter {i+1} element : "))
    newList.append(x)
searchTerm=int(input("Enter the term you want to search : "))
pos=binary(newList,0,n-1,searchTerm)
if (pos!=-1):
    print(f"{searchTerm} is present in position {pos}.")
else:
    print(f"{searchTerm} is not present in the list.")