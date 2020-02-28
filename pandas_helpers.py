import pandas as pd
from collections import Counter


def df_(x):
    return pd.DataFrame(x)


def sr(item):
    return pd.Series(item)


def vc(x):
    return x.value_counts()


def ri(df):
    return df.reset_index(drop=True)


def get_col_by_substring(df, substring):
    return [col for col in df.columns if substring in col.lower()]


def count_prefix(df, position=0):
    return Counter([col.split('_')[position] for col in df.columns]).most_common()