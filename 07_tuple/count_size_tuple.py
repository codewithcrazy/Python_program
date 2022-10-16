"""
Write a python program to create a tuple with
integer numbers 2,4,6,7,4,8,4. Display the counted
value of represented value 4.
"""
t = (2, 4, 6, 7, 4, 8, 4)
no=int(input("Enter the value you want to find - "))
count=0
for i in t:
    if no==i:
        count+=1
print(count)

# Alternate Method
# t = (2, 4, 6, 7, 4, 8, 4)
# cnt = t.count(4)
# print(cnt)