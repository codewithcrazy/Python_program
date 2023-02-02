# Write a program to test whether a given number is Fibonacci number or not.

n = int(input("Enter the number : "))
a=0
b=1

while(True):
    c=a+b
    a=b
    b=c
    if(n==c):
        print(f"{n} is a fibonacci number.")
        break
    elif(n<c):
        print(f"{n} is not a fibonacci number.")
        break



# # Alternate Method
# n = int(input("Enter the number : "))
# from math import sqrt
# def isPerfect(n):
#     x=sqrt(n)
#     if(x*x == n):
#         return True
#     return False

# x=5*n*n-4
# y=5*n*n+4
# if(n==0 or isPerfect(x) or isPerfect(y)):
#     print(f"{n} is a fibonacci number.")
# else:
#     print(f"{n} is not a fibonacci number.")
