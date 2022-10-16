# 2.Create two list static or dynamic. Display both the lists & perform the addition operation of two lists using their index & store into third list finally display the third list.
list = []
list1 = []
list2 = []
n=int(input("Enter the number of elements -\t"))
for i in range(0,n):
    print("Enter element ",i+1," in first list \t")
    x=int(input())
    list1.append(x)
for i in range(0,n):
    print("Enter element ",i+1," in second list \t")
    x=int(input())
    list2.append(x)
for i in range(0,len(list1)):
    add = list1[i] + list2[i]
    list.append(add)
print(list1)
print(list2)
print(list)
