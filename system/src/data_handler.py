import pandas as pd


class DataHandler:

    @staticmethod
    def get_jenga_session_dataframe() -> pd.DataFrame:
        df = pd.read_csv('./system/data/0001.csv')
        return df
