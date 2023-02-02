# Write a Python program to compute the reverse of a number using while loop.

num = int(input("Enter the number : "))

reverse=0
while(num!=0):
    rem=num%10
    reverse = reverse*10 + rem
    num = num//10
print(reverse)