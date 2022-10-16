# Write a program to pass a list in a function then return the sum.

def sum(list,n):
  sum=0
  for i in range(0,n):
    sum+=list[i]
  return sum

list=[]
n=int(input("Enter the size of the list -\t"))
for i in range(0,n):
  x=int(input(f"Enter element {i+1} -\t"))
  list.append(x)
print(f"Sum of the given list is {sum(list,n)} ")