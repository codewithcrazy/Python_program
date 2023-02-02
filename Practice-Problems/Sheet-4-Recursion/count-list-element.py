# Write a python program to count the number of elements in a List using user define recursive function.

def countList(lst):
    if(lst==[]):
        return 0
    lst.pop()
    return 1 + countList(lst)

lst = [1,2,3,4,5,6,7,8,9,10]
print(countList(lst))