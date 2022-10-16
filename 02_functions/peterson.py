# Write a program to display the peterson of a given number & check whether the number is peterson or not.

n = int(input("Enter the number -\t"))
temp=n
add=0
while(temp!=0):
    rem=temp%10
    fact=1
    for i in range(1,rem+1):
        fact=fact*i
    add=add+fact
    temp=temp//10  
print("The peterson value of {0} is {1}.".format(n,add))
if(add==n):
    print(n," is a peterson number.")
else:
    print(n," is not a peterson number.")