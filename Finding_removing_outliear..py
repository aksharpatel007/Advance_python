# finding and removing outliers

import pandas as pd
import numpy as np

df = pd.read_csv("auto-mpg.csv")
print(df)

# finding outliers

q1 = df['acceleration'].quantile(0.25)
q3 = df['acceleration'].quantile(0.75)

IQR = q3 - q1

low = q1 - (1.5*IQR)
high = q3 + (1.5*IQR)

print(low , high)

# outLiers = df[(df['acceleration'] < low) | (df['acceleration'] > high)]
# print(outLiers)

# removing outliers

removeOutliers = df[(df['acceleration'] >= low) & (df['acceleration'] <= high)]
print(removeOutliers)
