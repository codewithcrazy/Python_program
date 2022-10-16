"""
Write a program to input a string from the user & reverse that string .
Also check whether the string is palindrome or not.
"""
temp=""
str = input("Enter a string -\t")
for i in range(len(str)-1,-1,-1):
    temp=temp+str[i]

print(f"Reverse of {str} is {temp}")

if(str==temp):
    print(f"{str} is palindrome.")
else:
    print(f"{str} is not palindrome.")