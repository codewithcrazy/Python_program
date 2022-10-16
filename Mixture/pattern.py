def star():
    n = int(input("Enter the number of lines you want -\t"))
    for i in range(0, n+1):
        for j in range(0, n-i):
            print("*  ", end="")
        print("")


def rev_star():
    n = int(input("Enter the number of lines you want -\t"))
    for i in range(0, n+1):
        for j in range(0, i):
            print("*  ", end="")
        print("")

while(1):
    check=int(input("Enter 1 for star pattern, 2 for reverse and 3 for terminate -\t"))
    if(check==1):
        star()
    elif(check==2):
        rev_star()
    elif(check==3):
        break
    else:
        print("\nInvalid Input\n")
print("Game Terminated")