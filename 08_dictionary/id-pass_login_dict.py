"""
Write a python program to check user Id & password entered by the user & display proper output depending on correct or incorrect input.
If the password is correct display the message "Password  Matched" otherwise "Wrong password entered".
"""
d={}
check='y'
while(check == 'y' or check == 'Y'):
    userName=input("Enter User name -\t")
    password=input("Enter password -\t")
    d.update({userName:password})
    check=input("For continue press y....\t")
print("All data stored !\n",d)
userName=input("Enter your username -\t")
password=input("Enter your password -\t")
if(d.get(userName)!=None):
    if(d.get(userName)==password):
        print("Password Matched.")
    else:
        print("Wrong password entered.")
else:
    print("Wrong Username")