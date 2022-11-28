import numpy as np
r1=int(input("Enter the number of rows of first matrix:"))
c1=int(input("Enter the numnber of colums of first matrix:"))
a1=[]
for i in range(r1*c1):
        a1.append(int(input()))
a1=np.array(a1)
a1=a1.reshape(r1,c1)

r2=int(input("Enter the number of rows of second matrix:"))
c2=int(input("Enter the number of columns of second matrix:"))
a2=[]
for i in range(r2*c2):
        a2.append(int(input()))
a2=np.array(a2)
a2=a2.reshape(r2,c2)
print("First matrix:\n",a1)
print("Second matrix:\n",a2)
a3=a1+a2
print("Sum of matrix:\n",a3)


