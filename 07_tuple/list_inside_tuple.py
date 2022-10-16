"""
Write a python program consider a tuple where the tuple value are 3 different list.
List are [1,3],[2,6],[4,9] now make a tuple which includes the sum of individual list and display it.
"""
t=([1,3],[2,6],[4,9])
temp = []
for i in t:
    add=sum(i)
    temp.append(add)
t=tuple(temp)
print(t)