dict_student={}
dict_average={}
while(1):
    student_marks=[]
    temp=0
    student_name=input("Enter the student name -\t")
    for i in range(3):
        marks=int(input(f"Enter subject {i+1} marks - "))
        temp+=marks
        student_marks.append(marks)
    dict_student[student_name] = student_marks
    dict_average[student_name]=temp/3
    x=input("For continue enter y . . .  ")
    if(not(x=='y' or x=='Y')):
        print(dict_student)
        print(dict_average)
        break

max=0
for i in dict_average.items():
    if(max<i[1]):
        max=i[1]

print(f"{i[0]} has got maximum average marks i.e. {i[1]}")