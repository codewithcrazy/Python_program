employers_data=[]
for i in range(5):
    lst=[]
    name=input(f"Enter employer {i+1} name -\t")
    roll=int(input(f"Enter employer {i+1} roll -\t"))
    id_no=input(f"Enter employer {i+1} id -\t")
    salary=int(input(f"Enter employer {i+1} salary -\t"))
    phone_number=input(f"Enter employer {i+1} phone number -\t")
    lst.append(name)
    lst.append(roll)
    lst.append(id_no)
    lst.append(salary)
    lst.append(phone_number)
    employers_data.append(lst)
print(employers_data)
max=0
for i in employers_data:
    if(i[3]>max):
        max=i[3]
print(i)