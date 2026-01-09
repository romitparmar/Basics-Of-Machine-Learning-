import numpy as np

a1 = np.arange(0,14)
print(a1)
a2,a3,a4 = np.array_split(a1,[2,6])
print(a2)
print(a3)
print(a4)
