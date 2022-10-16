'''
4. Write a program to input e-mail id like abc@gmail.com & 
remove the letter '@' & all the other letters before '@' & print gmail.com . 
'''

email=input("Enter Email address -\t")
for i in range(0,len(email)):
    if(email[i]=='@'):
        break
print(email[i+1:])