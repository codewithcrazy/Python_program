"""
Write a program to input a string in smaller one.
the string should be combined of both vowels and consonents.
Remove all the vowels from it & print the modified string.
"""
str = input("Enter a string -\t").lower()
newStr = ""
vowel = ['a', 'e', 'i', 'o', 'u']
for ch in str:
    if ch not in vowel:
        newStr += ch
print(newStr)