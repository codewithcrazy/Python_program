"""
Write a program to print the following pattern:
A
B C
D E F
G H I J
"""

# n=int(input("Enter the number : "))
n=4
num=65

for i in range(n):
    for j in range(i+1):
        print(chr(num),end=" ")
        num+=1
    print("")