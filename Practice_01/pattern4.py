"""
Write a program to print the following pattern:
for n= 5
1
22
333
4444
55555
4444
333
22
1
"""

n=int(input("Enter the number : "))
for i in range(1,n+1):
    print(str(i)*i)
for i in range(n-1,0,-1):
    print(str(i)*i)