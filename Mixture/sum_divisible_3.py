# Write a program to take 4 digit any integer number from the keyboard then separate all the digits from the number then display all the digits which is divisible by 3 and calculate the sum of the digits which are divisible by 3.

n=int(input("Enter the number -\t"))
no=n
sum=0
while(no!=0):
    rem=no%10
    if(rem%3==0):
        print(rem)
        sum=sum+rem
    no=no//10
print(f"Sum of the number divisible by 3 is {sum}")