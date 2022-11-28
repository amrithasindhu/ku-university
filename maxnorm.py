import numpy as np
from numpy.linalg import norm
v=[]
l=int(input("Enter the number of values of vector:"))
print("Enter the values of vector")
for i in range(l):
    v.append(int(input()))
l1 = norm(v,np.inf)
print(l1)

