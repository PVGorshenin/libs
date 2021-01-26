from typing import Type

class DataframeChecker():

    @classmethod
    def check_dupl(self, df, col):
        assert not df[col].duplicated().sum().astype(bool)

    @classmethod
    def check_isnull(self, df, col):
        assert not df[col].isnull().sum().astype(bool)

    @classmethod
    def check_type(self ,df, col, type):
        assert df[col].map(lambda z: isinstance(z, type)).sum() == df.shape[0]

    @classmethod
    def check_nunique(self, df, col, unique_ratio):
        assert (df[col].nunique() / df.shape[0]) > unique_ratio

    @classmethod
    def check_all(self, df,  col: str, type: Type, unique_ratio=.5):
        self.check_dupl(df, col)
        self.check_isnull(df, col)
        self.check_type(df, col, type)
        self.check_nunique(df, col, unique_ratio)