"""Write a python program which accepts the radius of a circle
from the user and compute the Area and perimeter of a Circle."""

from math import pi
radius = int(input("Enter the radius of the circle - "))
area = pi * pow(radius,2)
perimeter = 2 * pi * radius

print(f"Area of the circle of radius {radius} is {area}")
print(f"Perimeter of the circle of radius {radius} is {perimeter}")