list=[]
new_list=[]
sum=0
for i in range(0,6):
    print(f"Enter element {i+1}")
    x=int(input())
    list.append(x)
print(f"You have entered -\t{list}")
for i in range(0,len(list)):
    if(list[i]%2==0):
        x=list[i]+3
        new_list.append(x)
    else:
        x=list[i]-1
        new_list.append(x)
print(f"New list is -\t{new_list}")
print("Odd Numbers present in the list is ")
for i in range(0,len(new_list)):
    if(new_list[i]%2==0):
        sum+=new_list[i]
    else:
        print(new_list[i])
print(f"Sum of all even number is {sum}")