# Write a program to print all prime numbers for the range 1 to n.

def isPrime(n):
    for i in range(2,n):
        if(n%i==0):
            break
    else:
        return n
    return 0

n = int(input("Enter the number : "))
for i in range(1,n+1):
    if(isPrime(i)):
        print(isPrime(i),end=" ")
