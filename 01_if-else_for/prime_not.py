# Write a program to check whether a given number is prime or not
no = int(input("Enter the number -\t"))
flag=1
for i in range(2,no//2):
    if(no%i==0):
        flag=0
        break
if flag==1:
    print(no," is a prime number\n")
else:
    print(no," is not a prime number\n")