from sklearn import preprocessing
import pandas as pd
smoking = pd.read_csv('smoking.csv')
print(smoking)
d = preprocessing.normalize(smoking)
scaled_df = pd.DataFrame(d,columns=)
scaled_df.head()

x_array = np.array(housing['total_bedrooms'])
normalized_arr = preprocessing.normalize([x_array])
print(normalized_arr)