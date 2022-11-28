import numpy as np
r1=int(input("enter the no of rows:"))
c1=int(input("enter the no of columns:"))
a1=[]
for i in range (r1*c1):
    a1.append(input())
a1=np.array(a1)
a1=a1.reshape(r1,c1)

a3=[]
for i in range(r1):
        for j in range(c1):
            sum=0
            sc=10
            sum +=int(a1[i][j])*sc
            a3.append(sum)
a3=np.array(a3)
a3=a3.reshape(r1,c1)
print("product:",a3)
