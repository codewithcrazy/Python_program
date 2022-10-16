# write a python program to display the sum of the given series
# 1 + 1/2 + 1/4 + 1/6 ......

n = int(input("Enter the value of n -\t"))
add=1
for i in range(1,n):
    add = add + (1/(i*2))
print("The Sum of the series till {0} is {1}".format(n,add))