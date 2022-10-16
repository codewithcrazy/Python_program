"""
2. Write a program to take a string which consists of 2 words & each word is separated by a space.
Display the string where 2nd one is comes first and 1st one is go second.
"""

str = input("Enter 2 words -\t")
for i in range(0,len(str)):
    if (str[i] == " "):
        break
str = str[i+1:] + str[i] + str[:i]
print(str)