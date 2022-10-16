# Write a python program to display the gcd of two number by recursion technique.

def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
a=int(input("Enter First number -\t"))
b=int(input("Enter Second number -\t"))
ans=gcd(a,b)
print("GCD of {0} and {1} is {2}".format(a,b,ans))