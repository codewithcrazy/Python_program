# Write a Python program to compute the factorial of given integer using function 

def fact(n):
    if(n>=2):
        return n*fact(n-1)
    return 1

n = int(input("Enter the number : "))
print(f"factorial of {n} is {fact(n)}")