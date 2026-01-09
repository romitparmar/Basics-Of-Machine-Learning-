import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([7,4,0])

result_arr = np.stack((arr1,arr2),axis=1)
print("The result Array is:- \n",result_arr)