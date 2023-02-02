# Write a python program to find the last element of a List using user define recursive function.

def lastEle(lst):
    if(len(lst)>1):
        return lastEle(lst[1:])
    return lst

lst = [1,2,3,4,5,6,7,8,9]
print(lastEle(lst))