# 3. Take a list with 10 integer number & display all even and odd numbers from the list also calculate the sum of all even numbers and the sum of all odd numbers
list=[0,1,2,3,4,5,6,7,8,9]
even_list=[]
even_sum=0
odd_list=[]
odd_sum=0
for i in range(0,len(list)):
    if(list[i]%2==0):
        even_list.append(list[i])
        even_sum+=list[i] 
    else:
        odd_list.append(list[i])
        odd_sum+=list[i]
print("Even numbers -\t",even_list)
print("Sum of all even numbers is ",even_sum)
print("Odd numbers -\t",odd_list) 
print("Sum of all odd numbers is ",odd_sum)
