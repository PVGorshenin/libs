import pandas as pd
from collections import Counter


def get_col_by_substring(df, substring):
    return [col for col in df.columns if substring in col.lower()]


def count_prefix(df, position=0):
    return Counter([col.split('_')[position] for col in df.columns]).most_common()