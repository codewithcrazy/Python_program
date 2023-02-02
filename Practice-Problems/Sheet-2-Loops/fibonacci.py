# Write a program to find all Fibonacci numbers after 100 but less than 1000.

a=0
b=1

while(True):
    c=a+b
    a=b
    b=c
    if(c<=100):
        continue
    elif(c>=1000):
        break
    print(c)
