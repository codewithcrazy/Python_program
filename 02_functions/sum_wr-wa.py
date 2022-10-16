# Write a program to display the addition of two float numbers using three different user defined function 
# (i) With return with argument

def add(a,b):
    c=a+b
    return c
a = float(input("Enter First number -\t"))
b = float(input("Enter Second number -\t"))
ans=add(a,b)
print("The sum of {0} and {1} is {2}.".format(a,b,ans))