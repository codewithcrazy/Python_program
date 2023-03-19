# Write a program to check whether a number is prime or not. 


n = int(input("Enter the number : "))

for i in range(2,n):
    if(n%i==0):
        print(f"{n} is not a prime number.")
        break
else:
    print(f"{n} is a prime number")