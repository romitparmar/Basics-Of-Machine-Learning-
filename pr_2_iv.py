import numpy as np

array1 = np.arange(2,11).reshape(3,3)
# print(array1)
print("after appending the elements!!!\n")
array1 = np.append(array1,[1,2,3]).reshape(4,3)
print(array1)
print("\n")
arr2 = array1.reshape(3,4)
print(arr2)