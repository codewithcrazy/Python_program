# Write a program to find factorial of a number.

n = int(input("Enter the number : "))
fact=1
for i in range(n+1):
    if(i>1):
        fact*=i
print(f"Factorial of {n} is {fact}.")