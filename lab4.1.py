from sklearn import preprocessing
import pandas as pd
import numpy as np
smoking = pd.read_csv("smoking.csv")
x_array = np.array(smoking['age'])
normalized_arr1 = preprocessing.normalize([x_array])
print('The normalized array of age ',normalized_arr1)
y_array = np.array(smoking['male'])
normalized_arr2 = preprocessing.normalize([y_array])
print('The normalized array of male', normalized_arr2)
z_array = np.array(smoking['sbp'])
normalized_arr3 = preprocessing.normalize([z_array])
print('The normalized array of sbp ',normalized_arr3)
p_array = np.array(smoking['smoker'])
normalized_arr4 = preprocessing.normalize([p_array])
print('The normalized array of smoker ',normalized_arr4)
