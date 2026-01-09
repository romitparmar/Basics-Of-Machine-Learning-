import pandas as pd

# Create a DataFrame with one row
dataFrate_1 = pd.DataFrame({
    1: ["x","a"],
    2: ["y","d"],
    3: ["z","t"]
})


series1 = dataFrate_1.iloc[:,0]
print(series1)


