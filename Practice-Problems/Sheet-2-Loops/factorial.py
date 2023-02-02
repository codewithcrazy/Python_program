# Write a Python program to compute the factorial of given integer 
# Input is never negative number

num = int(input("Enter the number : "))
fact = 1
for i in range(1,num+1):
    fact*=i
print(f"factorial of {num} is {fact}")