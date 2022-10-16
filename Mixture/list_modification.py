list=[]
sum=0
for i in range(0,6):
    print(f"Enter element {i+1}")
    x=int(input())
    list.append(x)
print("List is ",list)
for i in range (0,len(list)):
    if(list[i]%2==0):
        list[i]+=5
    else:
        list[i]+=-1
print("Modified List is ",list)
print("Number divisible by 5 are  ")

for i in range(0,len(list)):
    if(list[i]%5==0):
        print(list[i])
for i in range(0,len(list)):
    sum+=list[i]
print("Sum = ",sum)