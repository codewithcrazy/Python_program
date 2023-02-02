"""Write a program to compute the following sum using function:
1 + (1+2) +  (1+2+3) + (1+2+3+4) + .....  .....   ....  up to 10 terms."""
# output 220 -> n=10

def series(n):
    sum=0
    for i in range(1,n+1):
        sum+=add(i)
    return sum

def add(n):
    sum=0
    for i in range(n+1):
        sum+=i
    return sum

n = int(input("Enter the number : "))
print(series(n))