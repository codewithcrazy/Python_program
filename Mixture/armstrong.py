def count(n):
    cnt=0
    while(n!=0):
        n=n//10
        cnt=cnt+1
    return cnt
    
def arm(no):
    sum=0
    while(no!=0):
        rem=no%10
        sum=sum+pow(rem,count(n))
        no=no//10
    return sum
    
n=int(input("Enter the number -\n"))
sum=arm(n)
if(n==sum):
    print("ARM")
else:
    print("Not ARM")