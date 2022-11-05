"""
Write a python program to take a list with 12 elements where 3 different datas are repeated
atleast 2 times from the user input atleast 2 times from the user input now separate the 
list into two list of even and odd numbers without repetation of data. Display all the 3 
list and calculate the sum of even & odd list.
"""
lst=[]
new_list=[]
even_list=[]
odd_list=[]
even_sum=0
odd_sum=0

for i in range(12):
    x=int(input("Enter %d number -\t"%(i+1)))
    lst.append(x)

for i in lst:
    if i not in new_list:
        new_list.append(i)

for i in new_list:
    if(i%2==0):
        even_sum+=i
        even_list.append(i)
    else:
        odd_sum+=i
        odd_list.append(i)

print("\nGiven List is -\t",lst)

print("\nList contains even element is -\t",even_list)
print("Sum of terms in even list -\t",even_sum)

print("\nList contains odd element is -\t",odd_list)
print("Sum of terms in odd list -\t",odd_sum)