# Write a python program to find the following sum using user defined recursive function.
# S=1+2+3+   ... ... ....  +19+20.

def add(n):
    if(n==1):
        return 1
    return n + add(n-1)

n = int(input("Enter the number : "))
print(add(n))