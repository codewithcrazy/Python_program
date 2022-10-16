#Write a python program to find nth fibonacci numbers using user defined recursive function.

def fib(n):
  if(n==0 or n==1):
    return n
  else:
    return fib(n-1)+fib(n-2)

n=int(input("Enter the number"))

for i in range(n):
  print(fib(i))
