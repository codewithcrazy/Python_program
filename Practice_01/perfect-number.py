# Write a program to check whether a number is perfect number or not. 

add=0
n=int(input("Enter the number : "))
for i in range(1,n):
    if(n%i==0):
        add+=i
if(add==n):
    print(f"{n} is a perfect number.")
else:
    print(f"{n} is not a perfect number.")