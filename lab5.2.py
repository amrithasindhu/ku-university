import pandas as pd
df = pd.read_csv('file.csv')
dummies = pd.get_dummies(df.profession)
merged = pd.concat([df,dummies],axis='columns')
merged = merged.drop(['profession'],axis='columns')
print(merged.to_string())