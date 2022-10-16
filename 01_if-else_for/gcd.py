# Write a program to take two int values & find the gcd of these two numbers.
a=int(input("Enter First number\n"))
b=int(input("Enter Second number\n"))
sno=min(a,b)
gno=max(a,b)
for i in range(sno,0,-1):
    if(sno%i==0)and(gno%i==0):
        print("GCD of {0} and {1} is {2}".format(a,b,i))
        break

