import pandas as pd
data = {
  "rollnumber": [1,2,3,4,5],
  "name": ['athira','amritha','aiswarya','christy','sharon'],
  "mark1":[52,50,40,60,6],
  "mark2":[40,50,35,40,39],
  "mark3":[50,30,56,35,39]
}
df = pd.DataFrame(data)
print(df)
print()
print(df['name'].loc[df['mark1'].idxmax()],df['mark1'].loc[df['mark1'].idxmax()])
maxval2=df['name'].loc[df['mark2'].idxmax()],df['mark2'].loc[df['mark2'].idxmax()]
maxval3=df['name'].loc[df['mark3'].idxmax()],df['mark3'].loc[df['mark3'].idxmax()]
print(maxval2,maxval3)

