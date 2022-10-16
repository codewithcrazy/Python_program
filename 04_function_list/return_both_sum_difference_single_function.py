# Write a program to return both sum and difference of two numbers in a single function.

def fun(a,b):
  sum=a+b
  diff=a-b
  return (sum,diff)

a=int(input("Enter first number -  "))
b=int(input("Enter second number -  "))
a,b=fun(a,b)
print(f"The sum is {a} and difference is {b}")