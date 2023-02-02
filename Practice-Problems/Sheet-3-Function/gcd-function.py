# Write a program to calculate GCD of two numbers using function

def gcd(a,b):
    for i in range(a,2,-1):
        if(a%i==0 and b%i==0):
            return i

a = int(input("Enter First number : "))
b = int(input("Enter Second number : "))
print(f"GCD of {a} and {b} is {gcd(a,b)}")