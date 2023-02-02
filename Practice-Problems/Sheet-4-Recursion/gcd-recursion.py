# Write a program to calculate GCD of two numbers using user defined recursive function

def gcd(a,b):
    if(a%b==0):
        return b
    return gcd(b,a%b)

a = int(input("Enter First number : "))
b = int(input("Enter Second number : "))
print(f"GCD of {a} and {b} is {gcd(a,b)}")