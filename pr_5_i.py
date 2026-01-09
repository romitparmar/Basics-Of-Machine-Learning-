import numpy as np 

array1 = np.array([[1,2,3],[2,3,4]])
array2 = np.array([[1,2,3],[3,4,5]])

flatten_array = array1.flatten()

max_value = np.amax(flatten_array,axis=0)
# max_value = np.amax(flatten_array,axis=1)
print(max_value)

min_value = np.amin(flatten_array)
print(min_value)

# m_ean = np.mean((array1),axis=1)
# print(m_ean)

# std = np.std((array2),axis=1)
# print(std)

# var = np.var((array2),axis=1)
# print(var)

