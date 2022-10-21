"""
Write a python program to generate inch to cm by
dictionary to store conversion values from inch to
centimeters taking user input from the keyboard.
"""
d={}
check='y'
while(check=='y' or check=='Y'):
    inch=float(input("Enter the value in inch -\t"))
    cm=2.54*inch
    d.update({inch:cm})
    check=input("For continue press y...\n")
print(d)