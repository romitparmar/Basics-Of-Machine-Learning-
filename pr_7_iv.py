import pandas as pd

dt = {
    "name" : ["apple","samsung"],
    "model" : ["16","s24"],
    "chip" : ["m6","snapdragon"]
}


dataframe = pd.DataFrame(dt, index=[0,1])
print(dataframe)

dataframe.to_csv("rp.csv",index=True)
print("done rp.csv")