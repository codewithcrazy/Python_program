# write a python program to display the sum of the given series
# 1 - 1/2^2 + 1/3^2 - 1/4^2 ......

n=int(input("Enter the value of n -\t"))
add=0
for i in range(1,n+1):
    if(i%2==0):
        add = add - 1/pow(i,2)
    else:
        add = add + 1/pow(i,2)
print("The sum of the series till {0} is {1}.".format(n,add))