'''
1. Write a program to take a string from the keyboard which consist of atleast 12 character.
Display only the substring from anywhere which consist of exactly 4 character.
'''

while (1):
    str = input("Enter a string consist of more than 12 characters -\t")
    if (len(str) >= 12):
        break
print(str[:4])