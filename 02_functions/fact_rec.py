# Write a python program to display the factorial of a number by recursion technique.

def fact(n):
    if(n==0):
        return 1
    else:
        return n*fact(n-1)
n=int(input("Enter a number -\t"))
ans=fact(n)
print("Factorial of {0} is {1}".format(n,ans))