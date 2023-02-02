# Write a program to calculate GCD of two numbers using for loop.

fnum=int(input("Enter first number : "))
snum=int(input("Enter second number : "))

for i in range(fnum,0,-1):
    if(fnum%i==0 and snum%i==0):
        print(f"gcd of {fnum} & {snum} is {i}")
        break