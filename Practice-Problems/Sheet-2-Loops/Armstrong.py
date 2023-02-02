# Write a program to find whether the given number is an Amstrong number or not.

def noDigit(no):
    count=0
    while(no!=0):
        rem =no%10
        count+=1
        no=no//10
    return count

num = int(input("Enter the number : "))
no = num
sum=0
digit = noDigit(num)
while(no!=0):
    rem =no%10
    sum = sum + pow(rem,digit)
    no=no//10

if(num==sum):
    print(num," is an armstrong number.")
else:
    print(num," is not an armstrong number.")
