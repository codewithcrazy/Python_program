"""
Write a program to print the following pattern:
*****
****
***
**
*
"""

n=int(input("Enter the number : "))
for i in range(n,0,-1):
    print("*"*i)