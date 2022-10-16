num = int(input("Enter a number\n"))
prime=True
for i in range(2,num):
	if(num%i == 0):
		prime = False
		break

if prime:
	print("This is a Prime number")
else:
	print("This is not a Prime number")