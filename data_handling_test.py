import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import scatter_matrix

# %matplotlib inline


df = pd.read_csv('Foreign_Exchange_Rates.csv')

# add US column
df['US$'] = 1.0

# replace 'ND' as NULL
df = df.replace(['ND'], value=np.NaN)


# ---replace null value with nearest non-null value
def find_nearest_previous_non_null(series, index):
    idx_before = index - 1
    return helper1(idx_before, series)


def helper1(idx, series):
    if idx >= 0 and pd.isnull(series.iloc[idx]):
        return helper1(idx - 1, series)
    return series.iloc[idx]


def find_nearest_next_non_null(series, index):
    idx_after = index + 1
    return helper2(idx_after, series)


def helper2(idx, series):
    if idx < len(series) and pd.isnull(series.iloc[idx]):
        return helper1(idx + 1, series)
    return series.iloc[idx]


# Iterate over each column and replace null values with average of nearest non-null values
for col in df.columns:
    mask = df[col].isnull()
    for i, val in enumerate(mask):
        if val:
            nearest_before = find_nearest_previous_non_null(df[col], i)
            nearest_after = find_nearest_next_non_null(df[col], i)
            if pd.notnull(nearest_before) and pd.notnull(nearest_after):
                df.loc[i,col] = (float(nearest_before) + float(nearest_after)) / 2

# ---convert dtypes of columns to correct type
df['Time Serie'] = pd.to_datetime(df['Time Serie'])
for i in df.columns[1:]:
    df[i] = pd.to_numeric(df[i])

# check
print(df.isnull().sum())

# ---Data Frame is ready for use (df)

# ---rating of similarity
