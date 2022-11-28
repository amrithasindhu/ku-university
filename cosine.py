import numpy as np
from numpy.linalg import norm
v1=[]
v2=[]
n1=int(input("Enter the number of values of first vector:"))
print("Enter the values of vector")
for i in range(n1):
    v1.append(int(input()))
n2=int(input("Enter the number of values of second vector:"))
print("Enter the values of vector")
for i in range(n2):
    v2.append(int(input()))
print(v1,v2)
cosine = np.dot(v1,v2)/(norm(v1)*norm(v2))
print("Cosine Similarity:", cosine)


