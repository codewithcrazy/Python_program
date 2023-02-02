# Write a python program to find the sum of  integer elements of a List  using user defined  recursive function.

def addInt(lst):
    if(lst!=[]):
        if(int==type(lst[-1])):
            return lst.pop() + addInt(lst)
        else:
            lst.pop()
            return addInt(lst)
    return 0

lst = [0,"Hi",1,2,'d',3,"Hello","Python",4]
print(f"Sum of all integer in the list is {addInt(lst)}.")