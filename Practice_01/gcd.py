# Write a program to find gcd of a number.

n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))

for i in range(min(n1,n2)+1,0,-1):
    if(n1%i==0 and n2%i==0):
        print(f"GCD of {n1} and {n2} is {i}.")
        break
