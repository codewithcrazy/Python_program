"""
Write a program to print the following pattern:
A
A B
A B C
A B C D
"""

n=int(input("Enter the number : "))
for num in range(1,n+1):
    for i in range(ord("A"),int(ord("A"))+num):
        print(chr(i),end=" ")
    print("")
    