# Write a program to display the reverse of a given number & check whether the number is palindrome or not.
no = int(input("Enter the number -\t"))
n=no
add=0
while(n!=0):
    rem=n%10
    n=n//10
    add=add*10+rem
print("Reverse of ",no," is ",add)
if(add==no):
    print(no," is a palindrome number.")
else:
    print(no," is not a palindrome number.")