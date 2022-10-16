# 1. Create a list and number will be inserted by append function of a list. Display the list with n numbers & calculate the summation value of all list members by using sum function.

list = []
n=int(input("Enter the number of elements you want to push -\t"))
for i in range(0,n):
    print("Enter number ",i+1," \t")
    x=int(input())
    list.append(x)
print(list)
print(f"Sum of the list is {sum(list)}")