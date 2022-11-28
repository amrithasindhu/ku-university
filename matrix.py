import numpy as np
r=int(input("Enter the number of rows:"))
c=int(input("Enter the number of columns:"))
a=[]
for i in range(r*c):
        a.append(int(input()))
a=np.array(a)
a=a.reshape(r,c)
print(a)