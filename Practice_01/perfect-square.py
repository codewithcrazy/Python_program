# Write a program to check whether a number is perfect square or not.

n = int(input("Enter the number : "))
if(n==(n/2)*(n/2)):
    print(f"{n} is a perfect square.")
else:
    print(f"{n} is not a perfect square.")