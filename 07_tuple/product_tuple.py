"""
Write a python program to create a tuple with
integer numbers 1,5,6,7. Calculate product value of all list tuple
elements through a user define function.
"""
def product(t):
    p=1
    for i in t:
        p=p*i
    print(f"Product of {t} is {p}")

t=(1,5,6,7)
product(t)