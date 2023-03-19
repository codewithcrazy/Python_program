# Write a program to check whether a number is neon or not.

n = int(input("Enter the number : "))

sqno = n*n
sum=0

while (sqno != 0):
    rem = sqno % 10
    sum+=rem
    sqno = sqno//10

if(n==sum):
    print(f"{n} is a neon number.")
else:
    print(f"{n} is not a neon number.")