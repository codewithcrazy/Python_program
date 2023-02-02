# Write a python program for Sequential search  using  function.

def SequentialSearch(lst,searchEle):
    for i in range(len(lst)):
        if(searchEle==lst[i]):
            return i+1
    return -1

newList = []
n = int(input("Enter the number of Elements you want : "))
for i in range(n):
    x = int(input(f"Enter {i+1} element : "))
    newList.append(x)
searchEle = int(input("Enter the elements you want to search : "))
pos = SequentialSearch(newList, searchEle)
if (pos!=-1):
    print(f"{searchEle} is present in position {pos}.")
else:
    print(f"{searchEle} is not present in the list.")

