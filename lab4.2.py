from sklearn import preprocessing
import numpy as np
x_array = np.array([34,36,30,26,32,23])
normalized_arr = preprocessing.normalize([x_array])
print(normalized_arr)
