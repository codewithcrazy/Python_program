"""Write a Python program to get the difference between a given number
and 10 if the difference is positive then display the product of the given number
and 10 otherwise display their sum."""

num = int(input("Enter the number : "))
diff = num - 10

if(diff > 0):
    print(num*10)
else:
    print(num+10)