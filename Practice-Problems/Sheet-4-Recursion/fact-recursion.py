# Write a python program for factorial using user defined recursive function.

def fact(n):
    if(n<2):
        return 1 
    return n*fact(n-1)

n = int(input("Enter the number : "))
print(f"factorial of {n} is {fact(n)}.")