def check_one(n):
    flag=0
    while(n!=0):
        rem=n%10
        if(rem==1):
            flag=1
            break
        n=n//10
    return flag

n=int(input("Enter the number -\t"))
sum=0
chk=check_one(n)
if(chk==1):
    while(n!=0 and n%10!=1):
        rem=n%10
        print(rem)
        if(rem==1):
            break
        sum+=rem
        n=n//10
    if(n%10!=1):
        print(f"Sum is {sum}")