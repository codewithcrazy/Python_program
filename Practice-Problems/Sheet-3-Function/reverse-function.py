# Write a Python program to print the reverse of a number using function.

def reverse(n):
    print(n)
    if(n-1==0):
        return
    reverse(n-1)

n = int(input("Enter the number : "))
reverse(n)