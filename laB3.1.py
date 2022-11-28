import pandas as pd
from math import sqrt
df = pd.read_csv('smoking.csv')
print(df)

def findmean(column):
    sum=0
    l=len(column)
    for i in range(l):
        sum+=i
    avg=sum/l
print(avg)
print()




