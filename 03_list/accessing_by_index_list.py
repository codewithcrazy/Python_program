# Take a static list with the values of 1,3,5,6,'a','b','c',"hi". 
# (i) Print the 2nd and 4th index value
# (ii) Print the -1th and -4th index value
# (iii) Replace the list elements from 2nd to 4th index by 10,12,15
# (iv) Display the modified list
list=[1,3,5,6,'a','b','c',"hi"]
print("Element present in 2nd index value is {0} and in 4th is {1}.".format(list[2],list[4]))
print("Element present in -1th index value is {0} and in -4th is {1}.".format(list[-1],list[-4]))
print("Given list is {0}".format(list))
list[2:5]=[10,12,15]
print("Modified list is {0}".format(list))