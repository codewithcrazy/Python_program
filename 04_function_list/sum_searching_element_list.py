"""
Write a program to calculate the sum of searching element
in a static list
"""

#list=[5,7,12,19,32,47]
list=[5,7,5,9,10,11]
#list=[10,7,9,7,8,7]
sum=0
print("First List is ",list)
fnd=int(input("Enter the Searching element -\t"))

for i in range(0,len(list)):
  if(list[i]==fnd):
    sum+=list[i]
print(sum)