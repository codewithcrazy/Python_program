"""
Write a python program to calculate & display fibonacci series up to n terms by updating {1:0,2:1} dictionary whose key is s.no and value is corresponding fibonacci value.
"""
d={1:0,2:1}
n=int(input("Enter the number of terms you want in the dictionary- \n"))
for i in range(n-2):
    l = len(d)
    add = d.get(l-1) + d.get(l)
    d.update({l+1:add})
print(d)