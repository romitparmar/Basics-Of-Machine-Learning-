import pandas as pd


dt = pd.DataFrame({
    1: ["romit", "abc"],
    2: ["xyz", "def"]
})

delete1 = dt.pop(1)
print(dt)