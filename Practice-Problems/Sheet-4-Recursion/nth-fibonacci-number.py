# Write a program to find  n-th  Fibonacci numbers  using user defined  recursive function 

def fibonacci(n):
    if(n==0 or n==1):
        return n
    return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter the number : "))
print(fibonacci(n))