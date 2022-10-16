#Display the largest number among three different int values
a=int(input("Enter first number \n"))
b=int(input("Enter Second number \n"))
c=int(input("Enter Third number \n"))
if(a>b):
    if(a>c):
        print("Largest number among {0}, {1} and {2} is {0}".format(a,b,c))
    else:
        print("Largest number among {0}, {1} and {2} is {2}".format(a,b,c))
else:
    if(b>c):
        print("Largest number among {0}, {1} and {2} is {1}".format(a,b,c))
    else:
        print("Largest number among {0}, {1} and {2} is {2}".format(a,b,c))