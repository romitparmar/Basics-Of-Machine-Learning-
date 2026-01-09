import pandas as pd
import numpy as np

array1 = np.array([1,2,3],)
pd_series = pd.Series(array1,index=["monday","tuesday","thursday"])

print(pd_series)
