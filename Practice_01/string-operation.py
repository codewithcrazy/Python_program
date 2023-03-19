# Write a program to print number of vowels, consonants, digits and white spaces in a string.

string = input("Enter the string : ")

vowel=list("aeiouAEIOU")
digit=list("1234567890")

novowels = 0
noconsonants = 0
nodigits = 0
nospaces = 0

for ch in string:
    if ch in vowel:
        novowels+=1
    elif ch in digit:
        nodigits+=1
    elif(ch==" "):
        nospaces+=1
    elif ch not in vowel:
        noconsonants+=1
print(f"Given string is {string} contain :")
print("number of vowels = ",novowels)
print("number of consonents = ",noconsonants)
print("number of white spaces = ",nospaces)
print("number of digits = ",nodigits)