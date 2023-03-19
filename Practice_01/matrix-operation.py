# Write a program to print addition and subtraction of two matrices.

def printMatrix(a, r, c):
    for i in a:
        print(i)
    print("")

def matrixForm(r, c):
    a = []
    for i in range(1, r+1):
        temp = []
        for j in range(1, c+1):
            x = int(input(f"Enter [{i}][{j}] element : "))
            temp.append(x)
        a.append(temp)
    return a

def addMatrix(m1, m2, r, c):
    m = []
    for i in range(r):
        temp = []
        for j in range(c):
            x = m1[i][j]+m2[i][j]
            temp.append(x)
        m.append(temp)
    return m

row = int(input("Enter the number of rows : "))
column = int(input("Enter the number of column : "))

print("\nEnter the first matrix : ")
a = matrixForm(row, column)
print("\nEnter the first matrix : ")
b = matrixForm(row, column)

print("\nFirst matrix is :- ")
printMatrix(a, row, column)
print("\nSecond matrix is :- ")
printMatrix(b, row, column)

new = addMatrix(a, b, row, column)
print("\nNew Addition matrix is :- ")
printMatrix(new, row, column)