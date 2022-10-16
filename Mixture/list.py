# Write a program to take any 5 integer elements from the keyboard for a list then add integer value 5 with the elements which are present at even index of a list and subtract 2 from the element which are present at odd index and display all the modified element into another list.

list=[]
new_list=[]
for i in range(0,6):
    x=int(input("Enter the number -\t"))
    list.append(x)

print(f"Given list is {list}")

for i in range(0,len(list)):
    if(i%2==0):
        x=list[i]+5
        new_list.append(x)
    else:
        x=list[i]-2
        new_list.append(x)

print(f"MOdified list is {new_list}")