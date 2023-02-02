#  Write a program to find the all prime numbers below 100 using function.

def prime(n):
    for i in range(2,n):
        if(n%i==0):
            return False
    return True

i=1
while(True):
    if(i<100 and prime(i)):
        print(i,end="  ")
    elif(i==100):
        break
    i+=1