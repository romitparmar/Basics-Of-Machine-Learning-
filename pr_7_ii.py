import pandas as pd


dt = pd.DataFrame({
    1: ["romit", "abc"],
    2: ["xyz", "def"]
})

sorted1 = dt.sort_values(by=1,ascending=True)
print(sorted1)