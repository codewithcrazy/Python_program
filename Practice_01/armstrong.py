# Write a program to check whether a number is Armstrong or not.

def digit(no):
    digit=0
    while(no!=0):
        digit+=1
        no=no//10
    return digit


n = int(input("Enter the number : "))
no=n
temp=0
dgt=digit(n)
while(no!=0):
    rem = no%10
    temp += pow(rem,dgt)
    no=no//10

if(temp==n):
    print(f"{n} is an armstrong number.")
else:
    print(f"{n} is not an armstrong number.")