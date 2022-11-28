import numpy as np
r1=int(input("enter the no of rows:"))
c1=int(input("enter the no of columns:"))
a1=[]
for i in range (r1*c1):
    a1.append(input())
a1=np.array(a1)
a1=a1.reshape(r1,c1)
a2=a1
for i in range(r1):
        for j in range(c1):
            if (i<j):
                a1[i][j]=0
            else:
                a1[i][j]=a1[i][j]
print("Lower",a2)
for i in range(r1):
        for j in range(c1):
            if (i>j):
                a2[i][j]=0
            else:
                a2[i][j]=a2[i][j]
print("Upper",a2)