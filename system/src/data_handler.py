import pandas as pd


class DataHandler:

    @staticmethod
    def get_jenga_session_dataframe() -> pd.DataFrame:
        df = pd.read_csv('./system/data/tower_1.csv')
        return df
