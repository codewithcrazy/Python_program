# Write a program to enter a number and then calculate the sum of its digits 

num = int(input("Enter the number : "))
temp = num
sum=0
while(temp!=0):
    rem = temp%10
    sum+=int(rem)
    temp/=10
print(f"Sum of digits of {num} is {sum}")