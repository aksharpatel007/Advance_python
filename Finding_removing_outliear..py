import pandas as pd

df = pd.DataFrame({"Marks":[10,12,14,15,18,100]})

Q1 = df["Marks"].quantile(0.25)
Q3 = df["Marks"].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[(df["Marks"] < lower) | (df["Marks"] > upper)]
print(outliers)
