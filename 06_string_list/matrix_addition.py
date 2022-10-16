"""
3. Write a program to take two different matrix of int number of user specified order.
Display the resultant matrix by performing adddition of these two matrix.
"""

row=int(input("Enter the number of rows -\t"))
col=int(input("Enter the number of column -\t"))

a=[]
b=[]
ans=[]

for i in range(0,row):
    list=[]
    for j in range(0,col):
        x=int(input(f"Enter [{i+1}] [{j+1}] element -\t"))
        list.append(x)
    a.append(list)
    
for i in range(0,row):
    list=[]
    for j in range(0,col):
        x=int(input(f"Enter [{i+1}] [{j+1}] element -\t"))
        list.append(x)
    b.append(list)
    
for i in range(0,row):
    list=[]
    for j in range(0,col):
        x=a[i][j] +b[i][j]
        list.append(x)
    ans.append(list)

print("First matrix is :- ")
for i in a:
    print(i)

print("Second matrix is :- ")
for i in b:
    print(i)

print("Required matrix is :- ")
for i in ans:
    print(i)