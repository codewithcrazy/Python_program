# Write a Python program to print the calendar of a given month and year (Use ‘calendar’ module)

from calendar import month

yr = int(input("Enter the year : "))
mth = int(input("Enter the month : "))
print("\n",month(yr,mth))