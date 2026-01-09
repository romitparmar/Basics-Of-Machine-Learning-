import pandas as pd
import numpy as np

s1 = pd.Series([1,2,3,4])
std = np.std(s1)

print(std)