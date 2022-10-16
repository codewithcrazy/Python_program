#Factorial of first n natural number 
# factorial = 1*2*3*4*5*6*.....n

n = int(input("Enter The Number \n"))
fact= 1
for i in range(1,n+1):
	fact = fact*i
print(f"Factorial of {str(n)} is {fact}")