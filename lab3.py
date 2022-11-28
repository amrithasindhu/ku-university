import pandas as pd
import statistics
df = pd.read_csv('smoking.csv')
print(df.to_string())
print(df.mean().age)
