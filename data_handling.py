import pandas as pd
import numpy as np


def get_df():
    df = pd.read_csv('Foreign_Exchange_Rates.csv')
    df.insert(1, 'US$', 1.0)
    df = df.replace(['ND'], value=np.NaN)

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
                    df.loc[i, col] = (float(nearest_before) + float(nearest_after)) / 2

    # recursive:

    # ---convert dtypes of columns to correct type
    df['Time Serie'] = pd.to_datetime(df['Time Serie'])
    for i in df.columns[1:]:
        df[i] = pd.to_numeric(df[i])

    # check
    # print(df.isnull().sum())

    # ---Data Frame is ready for use (df)
    return df


def get_trend(column_name, df):
    def calc_slope(x):
        slope = np.polyfit(range(len(x)), x, 1)[0]
        return slope

    return df[df.columns[1:]].rolling(31536000, min_periods=2).apply(calc_slope)


def get_rating(column_name, df):
    result = get_trend(column_name, df)

    def assign_rating(base_value, other_value):
        base_sign = 1 if base_value >= 0 else -1
        other_sign = 1 if other_value >= 0 else -1
        diff = abs(base_value - other_value)

        if base_sign == other_sign:
            if diff < 0.0001:
                return 2
            elif diff < 0.01:
                return 1
        else:
            if diff < 0.0001:
                return -2
            elif diff < 0.01:
                return -1
        return 0

    ratings_df = pd.DataFrame(index=df.index, columns=df.columns[1:])
    for idx, row in result.iterrows():
        base_value = row[column_name]
        for col in result.columns:
            if col != column_name:
                other_value = row[col]
                rating = assign_rating(base_value, other_value)
                ratings_df.at[idx, col] = rating

    #recursive
    # def helper_rating_1():
    #     for idx, row in result.iterrows():
    #         base_value = row[column_name]
    #         return helper_rating_2()
    #
    #     return helper_rating_1()
    #
    # def helper_rating_2():
    #     if col != column_name:
    #         other_value = row[col]
    #         rating = assign_rating(base_value, other_value)
    #         ratings_df.at[idx, col] = rating
    #         return helper_rating_2()
    #     if col == last_col:
    #         return None

    return ratings_df
