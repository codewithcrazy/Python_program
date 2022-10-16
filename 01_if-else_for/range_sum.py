#To Take 5 different float values among these values the range belongs to 10.5 to 19.7 calculate the sumation of the numbers belongs to these range.
add=0
for i in range(1,6):
    a=float(input("Enter the number\n"))
    if(10.5<a<19.7):
        add=add+a
print("Sum is ",add)